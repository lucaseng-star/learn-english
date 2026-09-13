// 📋 话术搜索守卫 —— 跟 jwc-bot tests/quick-reply-search.test.js 同一组规则、同一组用例。
// 2026-09-13 Lucas 在原型里打 `/fcc` → 「没搜到」，跟 9 月 9 日在后台踩的同一个坑。守卫用 vm 真跑 app.js 里的函数，不 grep 字串。
// 跑：node app/quick-reply-search.test.js
const { strict: assert } = require('assert'); const fs = require('fs'); const path = require('path'); const vm = require('vm');
const SRC = fs.readFileSync(path.join(__dirname, 'app.js'), 'utf8');
let pass = 0, fail = 0; const t = (n, f) => { try { f(); console.log(`  ✅ ${n}`); pass++; } catch (e) { console.error(`  ❌ ${n}\n     ${e.message}`); fail++; } };
function extractFn(src, name) { const s = src.indexOf('function ' + name + '('); assert.ok(s >= 0, name + ' 不在 app.js'); let d = 0; for (let j = src.indexOf('{', s); j < src.length; j++) { if (src[j] === '{') d++; else if (src[j] === '}') { d--; if (d === 0) return src.slice(s, j + 1); } } throw new Error(name + ' 括号不闭合'); }
const ctx = { console }; vm.createContext(ctx);
vm.runInContext(extractFn(SRC, 'qrNormalizeQuery'), ctx); vm.runInContext(extractFn(SRC, 'qrMatches'), ctx);
const items = [
  { name: 'FCC Flow 5_Promotion', folder: 'FCC Flow', steps: [{ text: '☕ 周末咖啡基础班 RM1,299' }] },
  { name: 'BWC KL CN- S1 CONTENTS', folder: 'BWC KL CN', steps: [{ text: '🥯 周末烘焙课程!' }] },
  { name: 'Address', folder: '资料夹 9f2a', steps: [{ text: 'The Earth Bukit Jalil' }, { text: 'Waze link' }] },
];
const search = (raw) => items.filter(x => ctx.qrMatches(x, ctx.qrNormalizeQuery(raw))).map(x => x.name);
t('`/fcc` (ChatDaddy 斜线习惯) = 跟 `fcc` 一样命中', () => { assert.deepEqual(search('/fcc'), ['FCC Flow 5_Promotion']); assert.deepEqual(search('fcc'), ['FCC Flow 5_Promotion']); assert.deepEqual(search('//FCC '), ['FCC Flow 5_Promotion']); });
t('只打 `/` = 全部 (等于没搜)', () => { assert.equal(search('/').length, 3); assert.equal(search('').length, 3); assert.equal(search(undefined).length, 3); });
t('不分大小写 + 搜内文 + 搜第二步', () => { assert.deepEqual(search('bukit'), ['Address']); assert.deepEqual(search('waze'), ['Address']); assert.deepEqual(search('烘焙'), ['BWC KL CN- S1 CONTENTS']); });
t('资料夹名也搜得到', () => { assert.deepEqual(search('bwc kl'), ['BWC KL CN- S1 CONTENTS']); });
t('中间的 / 不剥 (只剥开头)', () => { assert.equal(search('kl/jb').length, 0); assert.equal(ctx.qrNormalizeQuery(' /a/b '), 'a/b'); });
t('renderTpls 真的用这两个 helper (防孤儿)', () => { const body = extractFn(SRC, 'renderTpls'); assert.ok(body.includes("qrNormalizeQuery($('#tplSearch').value)")); assert.ok(body.includes('qrMatches(t, q)')); assert.ok(!/toLowerCase\(\)\.includes\(q\)/.test(body), '旧的直接 toLowerCase 过滤不该还在'); });
t('示例话术里有 FCC 的模版 (Lucas 第一个就搜这个)', () => { const n = (SRC.match(/'FCC Flow [^']*'/g) || []).length; assert.ok(n >= 2, `只有 ${n} 条 FCC`); });
t("输入框打 `/` 会弹话术 (ChatDaddy 习惯)", () => { assert.ok(/v\.startsWith\('\/'\)\) return openDesk\(v, true\)/.test(SRC), '输入框的 / 触发不见了'); });
console.log(`\n${fail ? '❌' : '✅'} quick-reply-search: ${pass} pass, ${fail} fail`); process.exit(fail ? 1 : 0);
