// 把一条新的信息差条目追加到 data/info_gap.js 的 INFO_GAPS 数组最前（最新在前）。
// 用法: node scripts/add_gap.js '<JSON字符串>'
// JSON 需包含: id,date,type,title,gap,script,steps[],source
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const f = path.join(root, 'data', 'info_gap.js');

function fail(msg){ console.error('ERR: ' + msg); process.exit(1); }

if (process.argv.length < 3) fail('缺少条目 JSON 参数');
let entry;
try { entry = JSON.parse(process.argv[2]); }
catch (e) { fail('JSON 解析失败: ' + e.message); }

const required = ['id','date','type','title','gap','script','steps','source'];
for (const k of required) if (!(k in entry)) fail('条目缺少字段: ' + k);
if (!Array.isArray(entry.steps)) fail('steps 必须是数组');

let txt = fs.readFileSync(f, 'utf8');
const m = txt.match(/window\.INFO_GAPS\s*=\s*(\[[\s\S]*\]);/);
if (!m) fail('未找到 window.INFO_GAPS 数组');
let arr;
try { arr = JSON.parse(m[1]); }
catch (e) { fail('现有数组解析失败: ' + e.message); }

if (arr.some(g => g.id === entry.id)) { console.log('已存在相同 id，跳过: ' + entry.id); process.exit(0); }

arr.unshift(entry); // 最新在前
const out = 'window.INFO_GAPS = ' + JSON.stringify(arr, null, 2) + ';\n';
fs.writeFileSync(f, out);
console.log('OK 已追加: ' + entry.id + ' | 当前合集共 ' + arr.length + ' 条');
