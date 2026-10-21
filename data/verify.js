// 临时校验脚本（运行后删除）
const fs = require('fs');
global.window = {};
require('./english_daily.js');
require('./english_history.js');
const daily = global.window.ENGLISH_DAILY;
const history = global.window.ENGLISH_HISTORY;

let ok = true;
const log = (m) => console.log(m);

// 1. words count
const words = daily.words;
log('words.length = ' + words.length);
if (words.length !== 30) { ok = false; log('  !! words 数量不是 30'); }

// 2. word fields complete
for (const it of words) {
  for (const k of ['w','pos','p','cn','ex','exCn']) {
    if (!it[k]) { ok = false; log('  !! 缺字段 ' + k + ' in ' + JSON.stringify(it)); }
  }
}

// 3. collision with history (exclude today)
const today = daily.date;
const histWords = new Set();
for (const rec of history) {
  if (rec.date === today) continue;
  for (const w of rec.words) histWords.add(w.toLowerCase());
}
const collisions = words.map(w => w.w).filter(w => histWords.has(w.toLowerCase()));
log('history collision count = ' + collisions.length);
if (collisions.length) { ok = false; log('  !! 冲突词: ' + collisions.join(', ')); }

// 4. vocabArticle covers all 30 words (case-insensitive exact base match)
const vaText = daily.vocabArticle.paras.map(p => p.en).join(' ');
const missing = [];
for (const w of words) {
  const re = new RegExp('\\b' + w.w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\b', 'i');
  if (!re.test(vaText)) missing.push(w.w);
}
log('vocabArticle missing words = ' + missing.length);
if (missing.length) { ok = false; log('  !! vocabArticle 未覆盖: ' + missing.join(', ')); }

// 5. glossary count 25-30
log('glossary.length = ' + daily.article.glossary.length);
if (daily.article.glossary.length < 25 || daily.article.glossary.length > 30) { ok = false; log('  !! glossary 数量不在 25-30'); }

// 6. article para word counts 60-80
daily.article.paras.forEach((p, i) => {
  const n = p.en.trim().split(/\s+/).length;
  log('article para ' + (i+1) + ' words = ' + n + (n < 60 || n > 80 ? '  <-- 超出 60-80' : ''));
  if (n < 60 || n > 80) ok = false;
});

// 7. UTF-8 no BOM
for (const f of ['english_daily.js','english_history.js']) {
  const buf = fs.readFileSync(f);
  const bom = buf[0] === 0xEF && buf[1] === 0xBB && buf[2] === 0xBF;
  log(f + ' BOM=' + bom);
  if (bom) ok = false;
  // try decode
  try { buf.toString('utf8'); } catch(e) { ok = false; log(f + ' UTF-8 decode error'); }
}

log('=== RESULT: ' + (ok ? 'PASS' : 'FAIL') + ' ===');
