global.window = {};
require("./english_daily.js");
require("./english_history.js");

const daily = global.window.ENGLISH_DAILY;
const history = global.window.ENGLISH_HISTORY;

let ok = true;

// 1. words count
const words = daily.words.map(w => w.w);
console.log("words count =", words.length);
if (words.length !== 30) { ok = false; console.log("FAIL: words != 30"); }

// 2. structural fields
for (const f of ["date","topic","article","words","vocabArticle","grammar"]) {
  if (!(f in daily)) { ok = false; console.log("FAIL missing field:", f); }
}
console.log("date =", daily.date);
console.log("topic =", daily.topic);

// 3. article structure
const paras = daily.article.paras;
console.log("article paras =", paras.length);
paras.forEach((p,i) => {
  const wc = p.en.trim().split(/\s+/).length;
  if (wc < 60 || wc > 80) { ok = false; console.log("FAIL para", i, "word count", wc); }
  if (!p.cn) { ok = false; console.log("FAIL para", i, "missing cn"); }
});
console.log("glossary entries =", daily.article.glossary.length);

// 4. words fields completeness
daily.words.forEach(w => {
  for (const f of ["w","pos","p","cn","ex","exCn"]) {
    if (!(f in w)) { ok = false; console.log("FAIL word missing", f, JSON.stringify(w)); }
  }
});

// 5. vocabArticle coverage
const vaText = daily.vocabArticle.paras.map(p => p.en + " " + p.cn).join(" ").toLowerCase();
const missing = words.filter(w => !vaText.includes(w.toLowerCase()));
console.log("vocabArticle missing words =", missing.length, missing);
if (missing.length > 0) ok = false;

// 6. grammar
console.log("grammar items =", daily.grammar.length);
daily.grammar.forEach((g,i) => {
  if (g.options.length !== 4) { ok = false; console.log("FAIL grammar", i, "options != 4"); }
  if (typeof g.answer !== "number" || g.answer < 0 || g.answer > 3) { ok = false; console.log("FAIL grammar", i, "answer"); }
  if (!g.explain) { ok = false; console.log("FAIL grammar", i, "explain"); }
});

// 7. history overlap (exclude today's record)
const histWords = new Set();
history.forEach(rec => {
  if (rec.date === daily.date) return;
  (rec.words || []).forEach(w => histWords.add(w.toLowerCase()));
});
const overlap = words.filter(w => histWords.has(w.toLowerCase()));
console.log("history overlap (excl. today) =", overlap.length, overlap);
if (overlap.length > 0) ok = false;

// 8. duplicate words within daily
const dup = words.filter((w,i) => words.indexOf(w) !== i);
console.log("duplicate words in daily =", dup.length, dup);
if (dup.length > 0) ok = false;

console.log(ok ? "\nVALIDATION PASSED" : "\nVALIDATION FAILED");
