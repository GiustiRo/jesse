/* Shared rendering rules also exercised without a browser. */
(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.JesseFundingUI = api;
})(typeof globalThis === "object" ? globalThis : this, function () {
  "use strict";
  function fundingStatus(result) {
    if (!result || typeof result !== "object") {
      return { label: "Sin evidencia", tone: "neutral", detail: "Cargá una sesión para comprobar si contabilizó funding." };
    }
    const requested = result.requested_mode || result.mode;
    if (result.applied === true && result.mode === "historical") {
      return { label: "Funding aplicado", tone: "positive", detail: "El saldo y el resultado incluyen los pagos y cobros registrados. Un neto de cero también puede ser válido." };
    }
    if (requested === "disabled" && result.applied !== true) {
      return { label: "Funding desactivado", tone: "neutral", detail: "Esta sesión no modela pagos ni cobros de funding." };
    }
    if (requested === "historical" && result.applied !== true) {
      return { label: "Sin aplicación confirmada", tone: "warning", detail: "La configuración solicita funding, pero todavía no hay un resultado que confirme su aplicación." };
    }
    return { label: "Sin evidencia", tone: "warning", detail: "La sesión no contiene metadatos suficientes para confirmar el tratamiento de funding." };
  }
  function utcDate(value) {
    if (value === null || value === undefined || value === "") return "—";
    const date = new Date(Number(value));
    return Number.isFinite(date.getTime()) ? date.toISOString().replace("T", " ").replace(".000Z", " UTC") : "—";
  }
  function rate(value) {
    const number = Number(value);
    return value !== null && value !== undefined && Number.isFinite(number) ? `${(number * 100).toFixed(5)} %` : "—";
  }
  function money(value) {
    const number = Number(value);
    return value !== null && value !== undefined && Number.isFinite(number) ? `${number >= 0 ? "+" : ""}${number.toFixed(4)} USDT` : "—";
  }
  function escape(value) {
    return String(value ?? "").replace(/[&<>"']/g, character => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[character]));
  }
  return { fundingStatus, utcDate, rate, money, escape };
});
