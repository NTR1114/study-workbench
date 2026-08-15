const fs = require('fs');
const path = require('path');
const vm = require('vm');

const base = 'data';
const a = JSON.parse(fs.readFileSync(path.join(base, '_shard_a.json'), 'utf8'));
const b = JSON.parse(fs.readFileSync(path.join(base, '_shard_b.json'), 'utf8'));
const c = JSON.parse(fs.readFileSync(path.join(base, '_shard_c.json'), 'utf8'));
const d = JSON.parse(fs.readFileSync(path.join(base, '_shard_d.json'), 'utf8'));
const e = JSON.parse(fs.readFileSync(path.join(base, '_shard_e.json'), 'utf8'));

const obj = Object.assign({}, a, b);
obj.categories = Object.assign({}, c.categories, d.categories);
Object.assign(obj, e);

const out = 'window.FINANCE_DAILY = ' + JSON.stringify(obj, null, 2) + ';\n';

// 编码/乱码检测
const fffd = (out.match(/�/g) || []).length;
if (fffd > 0) { console.error('FFFD乱码数量=' + fffd); process.exit(1); }
if (out.indexOf('```') !== -1) { console.error('检测到markdown代码块标记'); process.exit(1); }
if (out.toLowerCase().indexOf('</script>') !== -1) { console.error('检测到</script>'); process.exit(1); }
if (!out.trim().endsWith(';')) { console.error('未以分号结尾'); process.exit(1); }

fs.writeFileSync(path.join(base, 'finance_daily.js'), out, 'utf8');

// 回读并执行校验
const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(out, ctx);
const fd = ctx.window.FINANCE_DAILY;
if (!fd || !fd.date) { console.error('window.FINANCE_DAILY 解析失败'); process.exit(1); }

const checks = [];
checks.push(['date', fd.date === '2026-08-15']);
checks.push(['updatedAt', typeof fd.updatedAt === 'string' && fd.updatedAt.indexOf('+08:00') !== -1]);
checks.push(['focus.gold', !!(fd.focus && fd.focus.gold && fd.focus.gold.value)]);
checks.push(['focus.hsi', !!(fd.focus && fd.focus.hsi && fd.focus.hsi.value)]);
checks.push(['focus.ixic', !!(fd.focus && fd.focus.ixic && fd.focus.ixic.value)]);
['gold','hsi','ixic'].forEach(k => {
  ['morning','afternoon','evening'].forEach(w => {
    const x = fd.focus[k].windows[w];
    checks.push([`focus.${k}.windows.${w}`, x && (x.dir==='up'||x.dir==='down'||x.dir==='flat') && !!x.note]);
  });
});
['morning','afternoon','evening'].forEach(w => {
  const x = fd.windows[w];
  checks.push([`windows.${w}.summary`, !!x.summary]);
  checks.push([`windows.${w}.buy>=5`, Array.isArray(x.buy) && x.buy.length >= 5]);
  checks.push([`windows.${w}.note`, !!x.note]);
});
['stocks','futures','funds','forex'].forEach(cat => {
  const x = fd.categories[cat];
  checks.push([`${cat}.hot=5`, Array.isArray(x.hot) && x.hot.length === 5]);
  checks.push([`${cat}.picks=5`, Array.isArray(x.picks) && x.picks.length === 5]);
  checks.push([`${cat}.orderflow.metrics=4`, Array.isArray(x.orderflow.metrics) && x.orderflow.metrics.length === 4]);
  x.picks.forEach((p,i) => {
    checks.push([`${cat}.pick[${i}].signal`, ['买入','卖出','持有','观望'].indexOf(p.signal) !== -1]);
    checks.push([`${cat}.pick[${i}].rating`, p.rating >= 1 && p.rating <= 5]);
  });
  x.orderflow.metrics.forEach((m,i) => {
    checks.push([`${cat}.ofmetric[${i}].dir`, ['up','down','flat'].indexOf(m.dir) !== -1]);
  });
});
checks.push(['sources>=20', Array.isArray(fd.sources) && fd.sources.length >= 20]);
checks.push(['disclaimer', !!fd.disclaimer]);

let ok = true;
let lines = out.split('\n').length;
checks.forEach(([name, pass]) => { if (!pass) { ok = false; console.error('FAIL: ' + name); } });
console.log('行数=' + lines + '  sources=' + fd.sources.length + '  FFFD=' + fffd + '  校验项=' + checks.length + (ok ? '  全部通过✅' : '  存在失败❌'));
if (!ok) process.exit(1);
console.log('OUTPUT_OK: ' + path.join(base, 'finance_daily.js'));
