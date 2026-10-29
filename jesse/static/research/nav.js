/* Mount on the dashboard shell, including direct hash navigation. */
(() => {
  'use strict';
  let view, loading, queued=false, registered=false;
  const isRoute=()=>/^#\/research\/?(?:\?|$)/.test(location.hash);
  function assets(){return loading||(loading=(async()=>{for(const name of ['logic','panel'])await new Promise((resolve,reject)=>{const s=document.createElement('script');s.src='/research/'+name+'.js';s.onload=resolve;s.onerror=reject;document.head.append(s);});})().catch(e=>{loading=null;throw e;}));}
  async function sync(){
    queued=false;
    // Register through the running Vue router. Unknown direct links otherwise
    // resolve to Nuxt's 404 before a dashboard <main> can be mounted.
    const router=document.querySelector('#__nuxt')?.__vue_app__?.config.globalProperties.$router;
    if(router&&!registered){
      registered=true;
      router.addRoute({path:'/research',name:'jesse-research',component:{render(){return null;}}});
      if(isRoute()){
        const nuxt=document.querySelector('#__nuxt').__vue_app__.$nuxt;
        // Clear only the missing-page error raised for this just-added route.
        if(nuxt?.payload.error?.statusCode===404)nuxt.payload.error=null;
        await router.replace('/research');schedule();return;
      }
    }
    for(const nav of document.querySelectorAll('nav')){
      if(!nav.querySelector('a[href^="#/"]'))continue;
      if(!nav.querySelector('[data-research-link]')){const a=document.createElement('a');a.href='#/research';a.dataset.researchLink='';a.textContent='Investigación';a.style.cssText='display:block;padding:10px 12px;font-size:14px;color:inherit';nav.append(a);}
    }
    if(view&&(!isRoute()||!view.parent.isConnected)){view.component?.destroy();view.host.remove();view.nodes.forEach(([n,hidden])=>{n.hidden=hidden;});view=undefined;}
    if(!isRoute())return;
    if(view){view.host.dataset.theme=document.documentElement.classList.contains('dark')?'dark':'light';return;}
    const main=document.querySelector('main');if(!main)return;
    const nodes=[...main.children].map(n=>[n,n.hidden]);nodes.forEach(([n])=>{n.hidden=true;});
    const host=document.createElement('section');host.id='jesse-research';host.style.padding='clamp(12px, 2.5vw, 28px)';host.dataset.theme=document.documentElement.classList.contains('dark')?'dark':'light';main.append(host);
    const current={parent:main,host,nodes};view=current;host.textContent='Cargando investigación…';
    try{await assets();if(view!==current)return;host.textContent='';current.component=window.JesseResearchPanel.mount(host.attachShadow({mode:'open'}));}catch{if(view===current)host.textContent='Error al cargar Investigación. Recargar la página para reintentar.';}
  }
  function schedule(){if(!queued){queued=true;requestAnimationFrame(sync);}}
  new MutationObserver(schedule).observe(document.documentElement,{childList:true,subtree:true,attributes:true,attributeFilter:['class']});
  window.addEventListener('hashchange',schedule);schedule();
})();
