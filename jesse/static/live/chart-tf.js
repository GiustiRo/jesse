(() => {
  const NOTE =
    "Cambiar 1m / 5m / 1h / 4h / 1D solo cambia el gráfico. La estrategia sigue en su temporalidad.";

  function onLivePage() {
    return location.pathname.startsWith("/live/");
  }

  function hideChartStrategyRows() {
    document.querySelectorAll("td, span, div, p").forEach((node) => {
      if (node.childNodes.length !== 1 || node.textContent !== "__chart__") return;
      const row = node.closest("tr") || node.closest("li") || node.parentElement;
      if (row) row.classList.add("jesse-chart-route");
    });
  }

  function ensureNote() {
    if (!onLivePage()) return;
    const chart = document.querySelector(".trade-history-chart, [class*='CandlesChart']")
      || document.querySelector("canvas")?.closest("div.relative");
    if (!chart) return;
    const host = chart.closest(".relative") || chart;
    if (getComputedStyle(host).position === "static") host.style.position = "relative";
    if (host.querySelector(".jesse-chart-tf-note")) return;
    const note = document.createElement("div");
    note.className = "jesse-chart-tf-note";
    note.textContent = NOTE;
    host.appendChild(note);
  }

  function sync() {
    hideChartStrategyRows();
    ensureNote();
  }

  const observer = new MutationObserver(() => sync());
  observer.observe(document.documentElement, { childList: true, subtree: true });
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", sync);
  } else {
    sync();
  }
})();
