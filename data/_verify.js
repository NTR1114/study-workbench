const fs = require('fs');
const path = require('path');

function load(file) {
  const full = path.join(__dirname, file);
  global.window = {};
  const code = fs.readFileSync(full, 'utf8');
  // encoding / replacement char check
  if (code.includes('�')) {
    console.log('FAIL: replacement char (U+FFFD) found in', file);
    process.exit(1);
  }
  // check for ASCII double quote inside Chinese text is hard; just eval
  const vm = require('vm');
  vm.runInThisContext(code);
  return global.window;
}

const daily = load('english_daily.js').ENGLISH_DAILY;
const hist = load('english_history.js').ENGLISH_HISTORY;

const dWords = daily.words.map(w => w.w);
console.log('date:', daily.date);
console.log('topic:', daily.topic);
console.log('article paras:', daily.article.paras.length);
console.log('glossary count:', daily.article.glossary.length);
console.log('words count:', dWords.length);
console.log('vocabArticle paras:', daily.vocabArticle.paras.length);
console.log('grammar count:', daily.grammar.length);

// word count assertion
if (dWords.length !== 30) { console.log('FAIL: words != 30'); process.exit(1); }

// unique words
if (new Set(dWords).size !== 30) { console.log('FAIL: duplicate words within day'); process.exit(1); }

// against history (exclude today's own record to avoid self-match)
const histWords = new Set();
hist.forEach(h => { if (h.date !== daily.date) h.words.forEach(w => histWords.add(w)); });
const overlap = dWords.filter(w => histWords.has(w));
if (overlap.length) { console.log('FAIL: overlap with history:', overlap); process.exit(1); }

// grammar answer index validity
daily.grammar.forEach((g, i) => {
  if (g.answer < 0 || g.answer >= g.options.length) { console.log('FAIL: grammar', i, 'answer out of range'); process.exit(1); }
});

// paragraph word counts (rough english token count)
daily.article.paras.forEach((p, i) => {
  const n = p.en.trim().split(/\s+/).length;
  console.log('article para', i+1, 'words:', n, (n>=60 && n<=80 ? 'OK' : 'OUT OF RANGE'));
});

// vocab article coverage
const vaText = daily.vocabArticle.paras.map(p => p.en).join(' ');
const missing = dWords.filter(w => !new RegExp('\\b'+w+'\\b', 'i').test(vaText));
console.log('words NOT used in vocabArticle:', missing);

console.log('ALL CHECKS PASSED');
