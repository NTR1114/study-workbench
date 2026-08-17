const fs = require('fs');
const vm = require('vm');
const path = require('path');
const f = path.join(__dirname, 'data', 'finance_daily.js');
const txt = fs.readFileSync(f, 'utf8');

// 1) FFFD / replacement char check
const fffd = (txt.match(/\uFFFD/g) || []).length;
console.log('FFFD count:', fffd);

// 2) markdown / script tags
console.log('has ``` :', txt.includes('```'));
console.log('has </script> :', txt.includes('</script>'));
console.log('ends with ; :', txt.trim().endsWith(';'));

// 3) execute in sandbox
const sandbox = { window: {} };
try {
  vm.runInNewContext(txt, sandbox, { timeout: 5000 });
} catch (e) {
  console.log('JS EXEC ERROR:', e.message);
  process.exit(1);
}
const D = sandbox.window.FINANCE_DAILY;
if (!D) { console.log('NO window.FINANCE_DAILY'); process.exit(1); }
console.log('date:', D.date, '| updatedAt:', D.updatedAt);

let checks = 0, fail = 0;
function ck(name, cond){ checks++; if(!cond){ fail++; console.log('FAIL:', name);} }

// top-level
ck('summary', typeof D.summary === 'string' && D.summary.length > 50);
ck('focus.gold', D.focus && D.focus.gold && D.focus.gold.value);
ck('focus.hsi', D.focus && D.focus.hsi && D.focus.hsi.value);
ck('focus.ixic', D.focus && D.focus.ixic && D.focus.ixic.value);
['gold','hsi','ixic'].forEach(k=>{
  const o = D.focus[k];
  ['name','value','signal','trend','analysis'].forEach(p=>ck(`focus.${k}.${p}`, !!o[p]));
  ['morning','afternoon','evening'].forEach(w=>{
    ck(`focus.${k}.windows.${w}.dir`, o.windows && o.windows[w] && ['up','down','flat'].includes(o.windows[w].dir));
    ck(`focus.${k}.windows.${w}.note`, o.windows && o.windows[w] && o.windows[w].note);
  });
});
['morning','afternoon','evening'].forEach(w=>{
  const o = D.windows[w];
  ck(`windows.${w}.summary`, !!o.summary);
  ck(`windows.${w}.buy>=5`, Array.isArray(o.buy) && o.buy.length>=5);
  ck(`windows.${w}.note`, !!o.note);
});
const cats = ['stocks','futures','funds','forex'];
cats.forEach(c=>{
  const o = D.categories[c];
  ck(`${c}.title`, !!o.title);
  ck(`${c}.analysis`, typeof o.analysis==='string' && o.analysis.length>50);
  ck(`${c}.hot=5`, Array.isArray(o.hot) && o.hot.length===5);
  ck(`${c}.picks=5`, Array.isArray(o.picks) && o.picks.length===5);
  o.picks.forEach((p,i)=>{
    ck(`${c}.pick${i}.signal`, ['买入','卖出','持有','观望'].includes(p.signal));
    ck(`${c}.pick${i}.rating1-5`, p.rating>=1 && p.rating<=5);
    ck(`${c}.pick${i}.prob`, !!p.probability);
  });
  ck(`${c}.orderflow.summary`, !!o.orderflow.summary);
  ck(`${c}.orderflow.metrics=4`, Array.isArray(o.orderflow.metrics) && o.orderflow.metrics.length===4);
  o.orderflow.metrics.forEach((m,i)=>{
    ck(`${c}.metric${i}.dir`, ['up','down','flat'].includes(m.dir));
  });
  ck(`${c}.orderflow.flow`, !!o.orderflow.flow);
});
ck('sources>=20', Array.isArray(D.sources) && D.sources.length>=20);
ck('disclaimer', !!D.disclaimer);

console.log(`\nSTRUCTURE CHECKS: ${checks} total, ${fail} fail`);
console.log('sources:', D.sources.length);
console.log('hot/picks per cat:',
  cats.map(c=>`${c}:${D.categories[c].hot.length}/${D.categories[c].picks.length}`).join(' '));
console.log('windows buy sizes:', ['morning','afternoon','evening'].map(w=>D.windows[w].buy.length).join('/'));
console.log(fail===0 ? '\nALL PASS ✅' : '\nHAS FAILURES ❌');
process.exit(fail===0?0:1);
