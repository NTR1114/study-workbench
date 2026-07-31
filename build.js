// 构建单文件版：把 data/*.js 内联进 index.html，输出到 dist/index.html
// 目的：部署到 GitHub Pages 后，手机端只需一次请求即可完整渲染，避免多脚本加载失败导致白屏。
const fs = require('fs');
const path = require('path');
const root = __dirname;

let html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
const files = ['english_daily.js', 'english_history.js', 'mystic_courses.js', 'draw_courses.js', 'grammar_course.js', 'finance_daily.js', 'info_gap.js', 'info_gap_pool.js'];

for (const f of files) {
  const content = fs.readFileSync(path.join(root, 'data', f), 'utf8');
  const tag = `<script src="data/${f}"></script>`;
  if (!html.includes(tag)) {
    console.error('未找到脚本标签:', tag);
    process.exit(1);
  }
  // 防止数据中出现 </script> 导致提前闭合（双写规避）
  const safe = content.replace(/<\/script>/gi, '<\\/script>');
  const inline = `<script>\n${safe}\n</script>`;
  html = html.replace(tag, inline);
}

// 兜底：若仍有外部 data 引用，提示
if (/<script src="data\//.test(html)) {
  console.error('仍存在未内联的 data 脚本');
  process.exit(1);
}

fs.mkdirSync(path.join(root, 'dist'), { recursive: true });
fs.writeFileSync(path.join(root, 'dist', 'index.html'), html);
console.log('✅ 单文件构建完成 -> dist/index.html (' + html.length + ' bytes)');
