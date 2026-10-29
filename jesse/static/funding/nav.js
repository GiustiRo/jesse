/* Extend the distributed dashboard without rewriting its generated Nuxt bundle.
 * The existing candles route, native form, sidebar and SPA history remain in place.
 * Our source-owned component is mounted inline and scoped with a ShadowRoot.
 */
(() => {
  "use strict";
  let view = null;
  let assets = null;
  let queued = false;
  const importRoute = () => /^#\/candles\/?(?:\?|$)/.test(location.hash);

  function loadScript(path) {
    return new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.src = path;
      script.onload = resolve;
      script.onerror = () => reject(new Error("No se pudo cargar el componente de datos."));
      document.head.appendChild(script);
    });
  }

  function loadAssets() {
    if (!assets) assets = (async () => {
      if (!window.JesseFundingUI) await loadScript("/funding/logic.js?v=2");
      if (!window.JesseFundingPanel) await loadScript("/funding/panel.js?v=3");
      const response = await fetch("/funding/index.html");
      if (!response.ok) throw new Error("No se pudo cargar el panel de datos.");
      const parsed = new DOMParser().parseFromString(await response.text(), "text/html");
      return parsed.querySelector("main").outerHTML;
    })().catch(error => { assets = null; throw error; });
    return assets;
  }

  function renameNavigation() {
    // Desktop and mobile have distinct sidebar instances. Preserve their router
    // links and icons; only replace the visible name and accessible label.
    document.querySelectorAll('nav a[href="#/candles/"],nav a[href="#/candles"]').forEach(link => {
      const label = link.querySelector('[data-slot="label"]') || [...link.querySelectorAll("span")].find(span => span.textContent.trim() === "Import Candles");
      if (label && label.textContent !== "Import Data") label.textContent = "Import Data";
      if (link.getAttribute("aria-label") === "Import Candles") link.setAttribute("aria-label", "Import Data");
      if (link.getAttribute("title") === "Import Candles") link.setAttribute("title", "Import Data");
    });
    document.getElementById("jesse-funding-nav")?.remove();
  }

  function teardown() {
    if (!view) return;
    view.component?.destroy();
    view.tabs.remove();
    view.host.remove();
    view.native.forEach(node => { node.hidden = false; node.removeAttribute("data-jesse-native-candles"); });
    if (view.actions) view.actions.hidden = false;
    view = null;
  }

  async function select(kind) {
    const current = view;
    if (!current) return;
    current.kind = kind;
    for (const button of current.tabs.querySelectorAll("button")) {
      const active = button.dataset.kind === kind;
      button.setAttribute("aria-selected", String(active));
      button.tabIndex = active ? 0 : -1;
    }
    current.native.forEach(node => { node.hidden = kind !== "candles"; });
    if (current.actions) current.actions.hidden = kind !== "candles";
    current.host.hidden = kind === "candles";
    if (kind === "candles") return;
    try {
      if (!current.component) {
        current.host.textContent = "Cargando datos…";
        const markup = await loadAssets();
        // A route can change while an asset loads. Never attach callbacks or
        // polling timers to a detached dashboard page.
        if (view !== current || !current.host.isConnected) return;
        if (current.kind === "candles") return;
        if (current.component) { current.component.selectKind(current.kind); return; }
        current.host.textContent = "";
        const shadow = current.host.attachShadow({ mode: "open" });
        shadow.innerHTML = '<link rel="stylesheet" href="/funding/panel.css?v=3"><link rel="stylesheet" href="/funding/embedded.css?v=3">' + markup;
        current.component = window.JesseFundingPanel.mount(shadow, { kind: current.kind });
      }
      current.component.selectKind(current.kind);
    } catch (error) {
      if (view === current) current.host.textContent = error.message;
    }
  }

  function sync() {
    queued = false;
    renameNavigation();
    if (view && (!view.container.isConnected || !importRoute())) teardown();
    if (!importRoute()) return;
    if (view) {
      view.host.dataset.theme = document.documentElement.classList.contains("dark") ? "dark" : "light";
      return;
    }
    const heading = [...document.querySelectorAll("main h3")].find(node => ["Import Candles", "Import Data"].includes(node.textContent.trim()));
    if (!heading) return;
    const header = heading.parentElement?.parentElement;
    const container = header?.parentElement;
    if (!container || container.tagName === "MAIN") return;
    const native = [...container.children].filter(node => node !== header);
    if (!native.length) return;
    heading.textContent = "Import Data";
    const description = heading.parentElement.querySelector("p");
    if (description) description.textContent = "Download candles, funding and open interest data for backtesting and research.";
    const tabs = document.createElement("div");
    tabs.id = "jesse-import-data-tabs";
    tabs.setAttribute("role", "tablist");
    tabs.setAttribute("aria-label", "Import data type");
    tabs.innerHTML = [["candles", "Candles"], ["funding", "Funding"], ["oi", "Open Interest"]].map(([kind, label]) => `<button type="button" role="tab" data-kind="${kind}" aria-selected="${kind === "candles"}" tabindex="${kind === "candles" ? "0" : "-1"}">${label}</button>`).join("");
    const host = document.createElement("section");
    host.id = "jesse-import-data-panel";
    host.setAttribute("role", "tabpanel");
    host.setAttribute("aria-label", "Funding and open interest data");
    host.hidden = true;
    host.dataset.theme = document.documentElement.classList.contains("dark") ? "dark" : "light";
    container.insertBefore(tabs, native[0]);
    container.appendChild(host);
    native.forEach(node => node.setAttribute("data-jesse-native-candles", ""));
    view = { container, tabs, host, native, actions: header.children[1], kind: "candles", component: null };
    view.actions?.setAttribute("data-jesse-candles-actions", "");
    tabs.addEventListener("click", event => {
      const button = event.target.closest("button[data-kind]");
      if (button) select(button.dataset.kind);
    });
    tabs.addEventListener("keydown", event => {
      if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) return;
      event.preventDefault();
      const buttons = [...tabs.querySelectorAll("button")];
      const index = buttons.indexOf(document.activeElement);
      const next = event.key === "Home" ? 0 : event.key === "End" ? buttons.length - 1 : (index + (event.key === "ArrowRight" ? 1 : -1) + buttons.length) % buttons.length;
      buttons[next].focus();
      select(buttons[next].dataset.kind);
    });
  }

  function schedule() {
    if (!queued) { queued = true; requestAnimationFrame(sync); }
  }
  const style = document.createElement("style");
  style.textContent = '#jesse-import-data-tabs{display:flex;gap:4px;border-bottom:1px solid var(--ui-border,#334155);margin:0 0 20px;overflow-x:auto}#jesse-import-data-tabs button{border:0;border-bottom:2px solid transparent;padding:10px 16px;background:transparent;color:inherit;font:inherit;font-size:14px;cursor:pointer;white-space:nowrap}#jesse-import-data-tabs button[aria-selected="true"]{border-bottom-color:#3b82f6;color:#3b82f6;font-weight:600}#jesse-import-data-tabs button:focus-visible{outline:2px solid #60a5fa;outline-offset:-2px}#jesse-import-data-panel[hidden],[data-jesse-native-candles][hidden],[data-jesse-candles-actions][hidden]{display:none!important}';
  document.head.appendChild(style);
  new MutationObserver(schedule).observe(document.documentElement, { childList: true, subtree: true, attributes: true, attributeFilter: ["class"] });
  window.addEventListener("hashchange", schedule);
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", schedule);
  else schedule();
})();
