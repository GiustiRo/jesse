/* Keep this source separate from the distributed Nuxt bundle, like the ARMAS panel. */
(() => {
  function mount() {
    const nav = document.querySelector('a[href="/live/"],a[href="/live"]')?.closest("nav") || document.querySelector("nav");
    if (!nav || document.getElementById("jesse-funding-nav")) return;
    const link = document.createElement("a");
    link.id = "jesse-funding-nav";
    link.href = "/funding/index.html";
    link.textContent = "Funding / OI";
    link.style.cssText = "display:block;padding:12px 8px;text-align:center;color:#93c5fd;font-size:11px;font-weight:600;border-top:1px solid #334155;";
    nav.appendChild(link);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mount);
  else mount();
  new MutationObserver(mount).observe(document.documentElement, { childList: true, subtree: true });
})();
