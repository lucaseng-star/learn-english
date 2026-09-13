/* 秒回 v4 —— 可用原型。示例数据；接真渠道时换下面的 adapter 层（见 README）。 */
(() => {
  'use strict';
  const NOW = Date.now();
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const ic = (id, cls = 'ic') => `<svg class="${cls}" aria-hidden="true"><use href="#${id}"/></svg>`;
  const hm = ms => { const d = new Date(ms); return `${String(d.getHours()).padStart(2,'0')}:${String(d.getMinutes()).padStart(2,'0')}`; };
  const ago = min => NOW - min * 60000;
  const hasCJK = s => /[一-鿿]/.test(s);

  /* ── 示例数据 ── */
  const ME = '你', ME_NAME = 'Boon', COLLEAGUE = '佳佳';
  const LINES = { emily: { label: 'Emily 线', emoji: '🍷', persona: 'Emily' }, cindy: { label: 'Cindy 线', emoji: '☕', persona: 'Cindy' }, coco: { label: 'Coco 线', emoji: '☕', persona: 'Coco' } };
  const STAGE = { hot: ['#dc2626', '热'], considering: ['#f0c040', '考虑中'], curious: ['#7fc6ff', '好奇'] };
  const SHARON_Q = '刚毕业。如果中途找到全职工作可以转周末班吗？学费怎么算？';
  const AINA_Q = 'Kelas Barista 1 hari tu hujung minggu ada tak? Berapa harga ya?';
  const CONVS = [
    { id: 'sharon', name: 'Sharon', line: 'emily', channel: 'wa', lang: 'zh', course: 'WNSM 调酒半工读', stage: 'hot', warn: '',
      botActive: true, sos: { question: SHARON_Q, askedAt: ago(14), claimedBy: null },
      messages: [
        { dir: 'in', at: ago(16), text: '你好 我看到调酒半工读的广告' },
        { dir: 'out', at: ago(16), by: 'Emily · Bot', text: '哈喽 Sharon，我是 Emily 🍷 调酒半工读是 9 个月 36 堂，一周上 1 天课，其余时间在合作酒吧带薪实习。你现在是在工作，还是刚毕业？', state: 'read' },
        { dir: 'in', at: ago(14), text: SHARON_Q } ],
      drafts: [
        { answer: '可以转，按剩余堂数折算', text: '可以的 Sharon，半工读转周末班随时可以，学费按剩余堂数折算，不会重复收。刚毕业的话建议先来看一堂实操（免费），这周六 2 点有一场，帮你留位？' },
        { answer: '先问：边找工作还是专心学', text: 'Sharon 你好，想先了解一下：你是想边找工作边学，还是先专心学完 9 个月？两种情况推荐的班不一样。' },
        { answer: '约通话 3 分钟', text: '这个问题电话讲 3 分钟更清楚。你现在方便吗？不方便的话晚上 8 点后我打给你。' } ] },
    { id: 'weijie', name: 'Wei Jie', line: 'cindy', channel: 'wa', lang: 'zh', course: 'BMART Diploma', stage: 'considering', warn: '',
      botActive: true, sos: { question: 'BMART diploma 是不是 PTPK 可以全额？我 SPM 只有 3 credit 够吗', askedAt: ago(8), claimedBy: COLLEAGUE, claimedAt: ago(6) },
      messages: [
        { dir: 'in', at: ago(10), text: '你好 想问 BMART diploma' },
        { dir: 'out', at: ago(10), by: 'Cindy · Bot', text: '你好 Wei Jie ☕ BMART Diploma 是 12 个月，咖啡 + 调酒 + 烘焙三合一。你是想转行，还是想开店？', state: 'read' },
        { dir: 'in', at: ago(8), text: 'BMART diploma 是不是 PTPK 可以全额？我 SPM 只有 3 credit 够吗' } ],
      drafts: [ { answer: 'PTPK 可全额，SPM 3 credit 够', text: 'Wei Jie 你好，BMART 可以申请 PTPK 全额，SPM 3 个 credit 符合门槛。需要身份证 + SPM 成绩单 + 两张照片，我们帮你办。要我先帮你预审吗？' } ] },
    { id: 'aina', name: 'Aina', line: 'coco', channel: 'wa', lang: 'bm', course: '1-Day Junior Barista', stage: 'curious', warn: '⚠ 不提酒精',
      botActive: true, sos: { question: '周末有场吗？多少钱？', askedAt: ago(4), claimedBy: null },
      messages: [
        { dir: 'in', at: ago(7), text: 'Hai, saya nampak iklan kelas barista. Untuk yang tak ada pengalaman boleh ke?', tr: '你好，我看到咖啡师课程的广告。没有经验的可以吗？' },
        { dir: 'out', at: ago(7), by: 'Coco · Bot', text: 'Hai Aina ☕ Boleh! Kelas 1 hari ni memang untuk yang baru nak mula.', state: 'read' },
        { dir: 'in', at: ago(4), text: AINA_Q, tr: '一日咖啡师课周末有场吗？多少钱？' } ],
      drafts: [
        { answer: '有周末场 · 下一场 19/9 · 报价', zh: '有！下一场周末 9 月 19 日周六 10–2 点，RM ___ 含材料和出席证明，要留位吗？', text: 'Ada! Sesi hujung minggu seterusnya 19 Sept (Sabtu), 10 pagi–2 petang. Harga RM ___ termasuk bahan & sijil kehadiran. Nak saya simpan tempat?' },
        { answer: '先问：几位一起来', zh: '报价前先问，一个人还是两个人来？双人价不同。', text: 'Sebelum saya bagi harga, awak datang seorang atau berdua? Harga berdua lain sikit.' },
        { answer: '约通话', zh: '电话讲 3 分钟更清楚，现在方便吗？', text: 'Senang kalau saya call 3 minit. Sekarang okay tak?' } ] },
    { id: 'jason', name: 'Jason Lim', line: 'cindy', channel: 'wa', lang: 'zh', course: 'BMART Diploma', stage: 'considering', warn: '⚠ 待核付款',
      botActive: false, receipt: { amount: 'RM 1,000', due: 'RM ___', askedAt: ago(7), done: false },
      messages: [
        { dir: 'in', at: ago(9), text: '好 我先付押金' },
        { dir: 'in', at: ago(8), image: true, text: '转好了', amount: 'RM 1,000.00' },
        { dir: 'out', at: ago(8), by: 'Cindy · Bot', text: '收到 Jason 🙏 我让同事核对一下，确认了马上发报名表给你。', state: 'read' } ],
      drafts: [] },
    { id: 'nurul', name: 'Nurul', line: 'coco', channel: 'ig', lang: 'bm', course: 'BWC Bakery Weekend', stage: 'considering', warn: '⚠ IG 窗口已关',
      botActive: false, windowClosed: 'ig', waNumber: '012-345 6789', handoff: { done: false, handle: '@nurul.bakes', account: 'Instagram · JWC Bakery' },
      messages: [
        { dir: 'in', at: ago(60 * 40), text: 'my number 012-345 6789, boleh call petang. Nak tanya pasal kelas roti weekend tu', tr: '我的号码 012-345 6789，下午可以打。想问周末面包课的事' } ],
      drafts: [ { answer: '下一场 27/9 · 转 WhatsApp', zh: '可以！下一场周末面包班 9 月 27 日，我等下 WhatsApp 你 🙂', text: 'Hai Nurul, boleh! Kelas Bakery Weekend seterusnya 27 Sept. Saya WhatsApp awak sekejap lagi ya 🙂' } ] },
    { id: 'kelvin', name: 'Kelvin Tan', line: 'cindy', channel: 'wa', lang: 'zh', course: '4-Day Barista Express', stage: 'hot', warn: '⚠ WhatsApp 窗口已关',
      botActive: false, windowClosed: 'wa', phone: '017-654 3210',
      messages: [ { dir: 'in', at: ago(60 * 50), text: '下个月的 4 日班几号开？我要先请假' } ],
      drafts: [ { answer: '10 月班 13 号开，留位到明天', text: 'Kelvin 你好，10 月班 13 号开，连续 4 天。名额我先帮你留着，明天前回我就行 👍' } ] },
  ];
  const HANDOFFS = [
    { id: 'nurul', name: 'Nurul', handle: '@nurul.bakes', account: 'Instagram · JWC Bakery', course: 'BWC Bakery Weekend', said: 'my number 012-345 6789, boleh call petang. Nak tanya pasal kelas roti weekend tu', number: '012-345 6789', at: ago(18), done: false },
    { id: 'farah', name: 'Farah', handle: '@farah.k', account: 'Facebook · JWC Academy 专页', course: 'FCC 周末咖啡班', said: '0176 543 210 这个是我的 WhatsApp，你 WhatsApp 我', number: '017-654 3210', at: ago(65), done: false },
  ];
  // 话术库：结构照 jwc-bot lib/quick-replies.js（ChatDaddy 1,001 个 flow 原名原文搬进来，全公司共用）。
  // 每条 = { name, folder, pinned, steps:[{ text, images, docs }], uses, cdFireCount }；{{name}} = 客户名。
  const T = (id, folder, name, text, o = {}) => ({ id, folder, name, pinned: !!o.pinned, uses: o.uses || 0, cdFireCount: o.fire || 0,
    steps: o.steps || [{ text, images: (o.images || []).map(f => ({ filename: f })), docs: (o.docs || []).map(f => ({ filename: f })) }] });
  const TEMPLATES = [
    T('t1', 'WNSM KL CN', 'WNSM KL CN- PRICE', '调酒半工读 WNSM 学费 RM ___ ，可分期 / PTPK。9 月班 16/9 开课，一周 1 天。图是课程表 👆', { pinned: true, uses: 132, images: ['WNSM-price.jpg'] }),
    T('t2', 'WNSM KL CN', 'WNSM KL CN- SCHEDULE 2026', '2026 年 WNSM 开课时间表在图里 👆 每期 9 个月，一周 1 天上课。', { uses: 87, images: ['WNSM-2026-1.jpg', 'WNSM-2026-2.jpg'] }),
    T('t3', 'WNSM KL CN', 'WNSM KL CN- INTERN BAR LIST', '半工读合作酒吧名单：KL 6 家、JB 2 家，按你住的地方安排。', { uses: 41 }),
    T('t4', 'WNSM KL CN', 'WNSM KL CN- BROCHURE', '完整课程简介在 PDF 里 👇 有问题直接问我。', { uses: 18, docs: ['WNSM 2026 Brochure.pdf'] }),
    T('t5', 'FCC Flow', 'FCC Flow 1_Intro', '', { fire: 310, steps: [
      { text: '嗨 {{name}} ☕ 周末咖啡班对吧？8 个周六，学完你能拉花 + 出一杯咖啡馆水准的咖啡。', images: [], docs: [] },
      { text: '想看「日期 / 真实学员评价 / 价格」哪个？我发你 😊', images: [], docs: [] } ] }),
    T('t6', 'FCC Flow', 'FCC Flow 3_Schedule', '10 月周末咖啡班：KL 周六 10/10 开，JB 周日 11/10 开。时间表在图里 👆', { fire: 96, images: ['FCC-schedule.jpg'] }),
    T('t7', 'FCC Flow', 'FCC Flow 5_Promotion', '☕ 周末咖啡基础班 RM1,299（原价 RM ___）到这个月底。含所有材料 + 证书。要帮你留位吗？', { pinned: true, fire: 205, images: ['FCC-promo.jpg'] }),
    T('t8', 'FMC WEEKEND KL CN', 'FMC WEEKEND KL CN- PRICE', '调酒周末班 FMC 学费 RM ___，2 个月 8 堂，每周 3 小时。', { uses: 64, images: ['FMC-price.jpg'] }),
    T('t9', 'BWC KL CN', 'BWC KL CN- PRICE', '🥯 周末烘焙班 RM ___，8 天，材料全包。', { uses: 22, images: ['BWC-price.jpg'] }),
    T('t10', 'BWC KL CN', 'BWC KL CN- S1 CONTENTS', '🥯 周末烘焙课程！第一堂：欧包基础 + 酵母。', { fire: 40 }),
    T('t11', 'WINE', 'WINE - 6450 (Emily)', '红酒初级课 · 5 款新世界红酒 · 2.5 小时 · RM ___。', { fire: 58, images: ['WINE-6450.jpg'] }),
    T('t12', '我的模版', 'KL 地址 + 停车', '校区在 The Earth, 22 Jln Jalil 1, Bukit Jalil，停车免费 3 小时。\nhttps://maps.app.goo.gl/FPwpepeCyvikiSUj6', { uses: 58 }),
    T('t13', '我的模版', 'PTPK 三样文件', 'PTPK 需要：身份证、最高学历证书、两张照片。我们帮你办。', { uses: 39 }),
    T('t14', 'Boon 常用', '周六试听', '{{name}} 欢迎来看一堂实操（免费），周六 2 点有一场，要帮你留位吗？', { uses: 22 }),
  ];
  const TPL_TOTAL = TEMPLATES.length;
  const tplStats = t => ({ images: t.steps.reduce((n, st) => n + st.images.length, 0), docs: t.steps.reduce((n, st) => n + st.docs.length, 0), steps: t.steps.length, uses: t.uses + t.cdFireCount });
  // 搜索规则照 jwc-bot dashboard.html 的 qrNormalizeQuery / qrMatches 原样：开头的 / 不算搜索字（ChatDaddy 习惯打 /fcc），名字 / 资料夹 / 每一步内文都搜，不分大小写
  function qrNormalizeQuery(raw) { return String(raw || '').trim().replace(/^\/+/, '').trim().toLowerCase(); }
  function qrMatches(x, q) { if (!q) return true; const has = (v) => String(v || '').toLowerCase().includes(q); return has(x.name) || has(x.folder) || (x.steps || []).some(st => has(st.text)); }
  const qrFill = (text, c) => String(text || '').replace(/\{\{\s*name\s*\}\}/gi, c ? c.name : '');

  /* ── 状态 ── */
  const state = { duty: true, filter: 'all', current: null, queue: null, draftOffset: {}, tplFolder: '', sentline: {}, lastNotif: 'sharon' };
  const conv = id => CONVS.find(c => c.id === id);
  const waitMin = at => Math.max(0, Math.round((Date.now() - at) / 60000));
  const level = m => m >= 10 ? 'hot' : m >= 5 ? 'warm' : 'cool';
  const isOpenSOS = c => c.sos && !c.sos.repliedAt;
  const mine = c => c.sos && c.sos.claimedBy === ME;
  const avatar = (c, sm) => `<span class="ava${sm ? ' ava--sm' : ''}"><span>${esc(c.name[0])}</span><i>${LINES[c.line].emoji}</i></span>`;
  const stageTag = k => `<span class="tag tag--gray stg"><i style="background:${STAGE[k][0]}"></i>${STAGE[k][1]}</span>`;

  let toastT; const toast = t => { $('#toastText').textContent = t; $('#toast').classList.add('is-on'); clearTimeout(toastT); toastT = setTimeout(() => $('#toast').classList.remove('is-on'), 1800); };
  const show = id => { ['login', 'queue'].forEach(s => { $('#' + s).hidden = s !== id; }); };

  /* ── 登录 ── */
  const loggedIn = () => { try { return localStorage.getItem('mh_user') || sessionStorage.getItem('mh_user'); } catch { return null; } };
  $('#remember').addEventListener('click', e => { const b = e.currentTarget; b.setAttribute('aria-checked', b.getAttribute('aria-checked') !== 'true'); });
  $('#loginForm').addEventListener('submit', e => {
    e.preventDefault();
    const name = $('#loginName').value.trim() || 'boon';
    try { ($('#remember').getAttribute('aria-checked') === 'true' ? localStorage : sessionStorage).setItem('mh_user', name); } catch {}
    show('queue'); renderQueue(); setTimeout(() => showNotif('sharon'), 700);
  });

  /* ── 通知 ── */
  let notifT;
  function showNotif(id) {
    const c = conv(id); if (!c || !isOpenSOS(c)) return;
    $('#nfName').textContent = c.name; $('#nfWait').textContent = `${waitMin(c.sos.askedAt)} 分`;
    $('#nfTime').textContent = hm(Date.now()); $('#nfBody').textContent = `${LINES[c.line].emoji} ${LINES[c.line].label} · ${c.sos.question}`;
    $('#notif').dataset.id = id; $('#notif').classList.add('is-on');
    clearTimeout(notifT); notifT = setTimeout(() => $('#notif').classList.remove('is-on'), 6000);
  }
  $('#notif').addEventListener('click', () => { $('#notif').classList.remove('is-on'); openChat($('#notif').dataset.id, 'notif'); });

  /* ── 待回 ── */
  function renderQueue() {
    const open = CONVS.filter(isOpenSOS);
    const counts = { all: open.length }; Object.keys(LINES).forEach(k => counts[k] = open.filter(c => c.line === k).length);
    $('#chips').innerHTML = [['all', '全部'], ...Object.entries(LINES).map(([k, v]) => [k, `${v.emoji} ${v.persona}`])]
      .map(([k, l]) => `<button class="chip" role="tab" data-f="${k}" aria-selected="${state.filter === k}">${l} <b class="num">${counts[k]}</b></button>`).join('');
    const rows = open.filter(c => state.filter === 'all' || c.line === state.filter).sort((a, b) => (a.sos.claimedBy === ME) - (b.sos.claimedBy === ME) || a.sos.askedAt - b.sos.askedAt);
    const replied = CONVS.filter(c => c.sos && c.sos.repliedAt && (state.filter === 'all' || c.line === state.filter));
    const row = c => {
      const m = waitMin(c.sos.askedAt); const other = c.sos.claimedBy && c.sos.claimedBy !== ME;
      const pill = c.sos.repliedAt ? `<span class="wait wait--cool">已回 ${hm(c.sos.repliedAt)}</span>` : `<span class="wait wait--${level(m)}">等 ${m} 分</span>`;
      const right = c.sos.repliedAt ? `<span class="who ${c.sos.claimedBy === ME ? 'who--me' : 'who--other'}">${c.sos.claimedBy === ME ? '你' : esc(c.sos.claimedBy)}回的</span>` : mine(c) ? `<span class="who who--me">你在回</span>` : other ? `<span class="who who--other">${esc(c.sos.claimedBy)} 在回</span>` : `<button class="zap" type="button" data-zap="${c.id}" aria-label="接手回复">${ic('i-bolt')}</button>`;
      return `<li class="qrow ${other ? 'is-other' : (!c.sos.claimedBy ? 'is-open' : '')}">${avatar(c)}<button class="qmain" type="button" data-open="${c.id}"><div class="qtop"><span class="qname">${esc(c.name)}</span>${pill}</div><p class="qsnip">${esc(c.sos.question)}</p><div class="qmeta"><span class="tag tag--blue">${esc(c.course)}</span>${stageTag(c.stage)}</div></button>${right}</li>`;
    };
    const receipts = CONVS.filter(c => c.receipt && !c.receipt.done).length;
    const handoffs = HANDOFFS.filter(h => !h.done).length;
    $('#qlist').innerHTML = `<li class="section">🆘 等真人 <b class="num">${rows.length}</b></li>`
      + (rows.length ? rows.map(row).join('') : '<li class="empty">没有客户在等</li>')
      + (replied.length ? `<li class="section">已回 · 等客户 <b class="num">${replied.length}</b></li>` + replied.map(row).join('') : '')
      + `<li><button class="linkrow" type="button" data-go="receipts">${ic('i-folder')}<span class="grow">待确认收款</span><b>${receipts}</b>${ic('i-chevron', 'ic ic--sm chev')}</button></li>`
      + `<li><button class="linkrow" type="button" data-go="handoff">${ic('i-phone')}<span class="grow">IG/FB 给了号码</span><b>${handoffs}</b>${ic('i-chevron', 'ic ic--sm chev')}</button></li>`;
    const unclaimed = open.filter(c => !c.sos.claimedBy).length;
    $('#queueN').textContent = `· ${unclaimed} 条`; $('#startQueue').disabled = !unclaimed;
    $('#duty').classList.toggle('is-off', !state.duty); $('#duty').querySelector('span').textContent = state.duty ? '值班中' : '已下班';
    $('#dutyline').innerHTML = state.duty ? '值班：<b>你、佳佳</b>' : '值班：<b>佳佳</b> · 你已下班，不收通知';
    $('#dutyLabel').textContent = state.duty ? '下班（不收通知）' : '上班（收通知）';
  }
  $('#chips').addEventListener('click', e => { const b = e.target.closest('[data-f]'); if (b) { state.filter = b.dataset.f; renderQueue(); } });
  $('#qlist').addEventListener('click', e => {
    const z = e.target.closest('[data-zap]'); if (z) return openChat(z.dataset.zap, 'zap');
    const o = e.target.closest('[data-open]'); if (o) return openChat(o.dataset.open, 'queue');
    const g = e.target.closest('[data-go]');
    if (g && g.dataset.go === 'receipts') { const c = CONVS.find(x => x.receipt && !x.receipt.done); return c ? openChat(c.id, 'queue') : toast('没有待确认的收款'); }
    if (g && g.dataset.go === 'handoff') return openHandoff();
  });
  $('#duty').addEventListener('click', () => { state.duty = !state.duty; renderQueue(); toast(state.duty ? '值班中 · 会收到 SOS 通知' : '已下班 · 不再收通知'); });
  $('#startQueue').addEventListener('click', () => {
    const ids = CONVS.filter(c => isOpenSOS(c) && !c.sos.claimedBy).sort((a, b) => a.sos.askedAt - b.sos.askedAt).map(c => c.id);
    if (!ids.length) return; state.queue = { ids, i: 0 }; openChat(ids[0], 'zap');
  });

  /* ── 设置 ── */
  const setGlobal = open => { $('#settingsSheet').classList.toggle('is-open', open); $('#scrimGlobal').classList.toggle('is-open', open); };
  $('#settings').addEventListener('click', () => setGlobal(true));
  $('#scrimGlobal').addEventListener('click', () => setGlobal(false));
  $('#settingsSheet').addEventListener('click', e => {
    const b = e.target.closest('[data-set]'); if (!b) return; setGlobal(false);
    if (b.dataset.set === 'duty') $('#duty').click();
    if (b.dataset.set === 'replay') { const c = CONVS.find(x => isOpenSOS(x) && !x.sos.claimedBy); c ? showNotif(c.id) : toast('没有待认领的 SOS'); }
    if (b.dataset.set === 'logout') { try { localStorage.removeItem('mh_user'); sessionStorage.removeItem('mh_user'); } catch {} show('login'); }
  });

  /* ── 会话 ── */
  function openChat(id, via) {
    const c = conv(id); if (!c) return;
    if (c.sos && !c.sos.repliedAt && !c.sos.claimedBy && (via === 'notif' || via === 'zap')) { c.sos.claimedBy = ME; c.sos.claimedAt = Date.now(); c.botActive = false; }
    state.current = id; state.sentline[id] = state.sentline[id] || null;
    $('#notif').classList.remove('is-on'); clearTimeout(notifT);
    $('#input').value = ''; autosize();
    renderChat(); closeOverlays();
    $('#chat').classList.add('is-open');
    if (via === 'notif') setTimeout(() => $('#input').focus(), 300);
  }
  function closeChat() { $('#chat').classList.remove('is-open'); closeOverlays(); state.current = null; renderQueue(); }
  function bubble(m) {
    const t = hm(m.at);
    if (m.image && m.dir === 'in') return `<div class="msg in"><div class="bubble img"><div class="pic">${ic('i-image', 'ic ic--lg')}<span>银行转账截图</span><b class="num">${esc(m.amount)} · ${t}</b></div><div class="cap">${esc(m.text)}</div><span class="meta num">${t}</span></div></div>`;
    if (m.image || m.doc) return `<div class="msg out"><div class="bubble img"><span class="by">${esc(m.by)}</span><div class="pic${m.doc ? ' pic--doc' : ''}">${m.doc ? '📎' : ic('i-image', 'ic ic--lg')}<b>${esc(m.file)}</b></div>${m.text ? `<div class="cap">${esc(m.text)}</div>` : ''}<span class="meta num">${t}${ic('i-check2', 'ic tick')}</span></div></div>`;
    if (m.dir === 'in') return `<div class="msg in"><div class="bubble${m.tr ? ' has-tr' : ''}"><p>${esc(m.text)}</p>${m.tr ? `<p class="tr"><b>译</b> ${esc(m.tr)}</p>` : ''}<span class="meta num">${t}</span></div></div>`;
    const meta = m.state === 'failed' ? `<span class="meta fail">❌ 未送达</span>` : m.state === 'pending' ? `<span class="meta num">发送中 ${ic('i-clock', 'ic tick')}</span>` : `<span class="meta num">${t}${ic('i-check2', 'ic tick')}</span>`;
    return `<div class="msg out"><div class="bubble"><span class="by">${esc(m.by)}</span><p>${esc(m.text)}</p>${meta}</div></div>`;
  }
  function failCard(c) {
    if (c.windowClosed === 'ig') return `<div class="failcard"><h4>❌ IG 窗口已关，发不出去</h4><p>她留了 WhatsApp 号码，改用：</p><div class="acts"><button class="big" type="button" data-fail="wa">${ic('i-wa', 'ic ic--sm')}&nbsp;WhatsApp 她 · ${esc(c.waNumber)}</button><div class="two"><button class="soft" type="button" data-fail="call">${ic('i-phone', 'ic ic--sm')}打电话</button><button class="soft" type="button" data-fail="wait">等她再发来</button></div></div></div>`;
    return `<div class="failcard"><h4>❌ WhatsApp 窗口已关，发不出去</h4><p>超过 24 小时只能发模板，他一回就能正常聊。</p><div class="acts"><button class="big" type="button" data-fail="tpl">发唤醒模板「课程更新」<small>这段话存成草稿，他回来一键发</small></button><div class="two"><button class="soft" type="button" data-fail="call">${ic('i-phone', 'ic ic--sm')}打电话 ${esc(c.phone)}</button><button class="soft" type="button" data-fail="wait">等他再发来</button></div></div></div>`;
  }
  function renderChat() {
    const c = conv(state.current); if (!c) return;
    const L = LINES[c.line]; const other = c.sos && c.sos.claimedBy && c.sos.claimedBy !== ME && !c.sos.repliedAt;
    $('#chatAva').innerHTML = `<span>${esc(c.name[0])}</span><i>${L.emoji}</i>`;
    $('#chatName').textContent = c.name; $('#chatLine').textContent = `${L.emoji} ${L.label}${c.channel === 'ig' ? ' · IG' : ''}`;
    const stt = $('#chatStatus');
    if (other) { stt.textContent = `${c.sos.claimedBy} 在回`; stt.className = 'chipst tag--gray'; }
    else if (c.botActive) { stt.textContent = 'Bot 在回'; stt.className = 'chipst tag--yellow'; }
    else { stt.textContent = 'Bot 已停'; stt.className = 'chipst tag--green'; }
    $('#ctx').innerHTML = `<b>${esc(c.course)}</b><i>·</i><b>${c.lang === 'bm' ? 'BM' : c.lang === 'en' ? 'EN' : '中文'}</b><i>·</i><b>${STAGE[c.stage][1]}</b>${c.warn ? `<i>·</i><span class="warn">${esc(c.warn)}</span>` : ''}`;
    const failed = c.messages.some(m => m.state === 'failed');
    $('#streamInner').innerHTML = `<span class="daysep">${c.windowClosed ? '前天' : '今天'}</span>` + c.messages.map(bubble).join('') + (failed ? failCard(c) : '');
    const st = $('#stream'); st.scrollTop = st.scrollHeight;
    // 输入框上方
    let above = '';
    if (c.receipt && !c.receipt.done) {
      above += `<div class="taskwrap"><div class="task task--warm"><div class="th">💳 客户付了？<span class="wait wait--warm num">等了 ${waitMin(c.receipt.askedAt)} 分</span></div><div class="grid"><div><small>课程</small><b>${esc(c.course.split(' ')[0])}</b></div><div><small>应付押金</small><b class="num">${esc(c.receipt.due)}</b></div><div><small>图里金额</small><b class="num">${esc(c.receipt.amount)}</b></div></div></div></div>`;
      above += `<div class="actions"><button class="big" type="button" data-rc="ok">✅ 确认收款<small>${L.persona} 自动发报名表</small></button><div class="two"><button class="soft danger" type="button" data-rc="no">❌ 不是付款</button><button class="soft" type="button" data-rc="reply">先回一句</button></div></div>`;
    } else if (isOpenSOS(c)) {
      const m = waitMin(c.sos.askedAt);
      above += `<div class="taskwrap"><div class="task task--${level(m)}"><div class="th">客户在问<span class="wait wait--${level(m)} num">等了 ${m} 分</span></div><div class="tq">${esc(c.sos.question)}</div></div></div>`;
      if (!c.botActive && !other && c.drafts.length) {
        const off = state.draftOffset[c.id] || 0; const ds = [0, 1].map(i => c.drafts[(off + i) % c.drafts.length]).filter((d, i, a) => a.indexOf(d) === i);
        above += `<div class="drafts"><div class="dh">${ic('i-asterisk', 'ic ic--sm')}草稿<button type="button" id="moreDrafts">换一批</button></div><div class="drow">${ds.map((d, i) => `<button class="draft" type="button" data-draft="${c.drafts.indexOf(d)}"><b>${esc(d.answer)}</b><p>${esc(d.zh || d.text)}</p>${d.zh ? `<small>BM：${esc(d.text)}</small>` : ''}</button>`).join('')}</div></div>`;
      }
    }
    const txt = $('#input').value;
    if (c.lang !== 'zh' && txt.trim() && hasCJK(txt)) {
      const d = c.drafts.find(x => x.zh === txt.trim());
      above += `<div class="trstrip"><b>发出时翻成 ${c.lang.toUpperCase()} ✓</b><span>${esc(d ? d.text : '接入后自动翻译（示例先按原文发）')}</span><button type="button" id="sendZh">发中文</button></div>`;
    }
    const sl = state.sentline[c.id];
    if (sl) above += `<div class="sentline">${ic('i-check2')}<span><b>已发 ✓✓</b><i> · ${c.channel === 'ig' ? '已转人手，Bot 不会自动回来' : '12 小时后 Bot 接回'}</i></span><button type="button" id="handback">🟢 ${c.channel === 'ig' ? '让 Bot 接管' : '交还'}</button></div>`;
    if (c.botActive && !c.receipt) above += `<button class="gate" type="button" id="gate"><span>${other ? `${esc(c.sos.claimedBy)} 在回` : 'Bot 还在回，先停它'}</span><em>${other ? '我接手' : '🔴 停 bot 并回复'} ${ic('i-chevron', 'ic ic--sm')}</em></button>`;
    $('#above').innerHTML = above;
    const comp = $('#composer'); comp.classList.toggle('is-off', !!(c.botActive && !c.receipt));
    $('#input').placeholder = c.windowClosed === 'ig' && failed ? 'IG 现在发不出去' : c.windowClosed === 'wa' && failed ? '现在只能发模板' : `以 ${L.persona} 的身份回复…`;
    $('#send').disabled = !$('#input').value.trim();
    let below = '';
    if (state.queue && sl) { const nx = nextInQueue(); below = nx ? `<div class="nextbar"><div><i>下一条</i> ${esc(nx.name)} · ${LINES[nx.line].emoji} ${LINES[nx.line].label} · <b class="num">等 ${waitMin(nx.sos.askedAt)} 分</b></div><button type="button" id="next">下一条 ${ic('i-chevron', 'ic ic--sm')}</button></div>` : `<div class="nextbar"><div><i>队列清空</i> 没有人在等了</div><button type="button" id="next">回列表</button></div>`; }
    $('#belowComposer').innerHTML = below;
  }
  function nextInQueue() { return CONVS.filter(c => isOpenSOS(c) && !c.sos.claimedBy).sort((a, b) => a.sos.askedAt - b.sos.askedAt)[0] || null; }

  function autosize() { const i = $('#input'); i.style.height = 'auto'; i.style.height = Math.min(i.scrollHeight, 132) + 'px'; }
  function insert(text) { $('#input').value = text; autosize(); $('#send').disabled = !text.trim(); renderChat(); $('#input').focus(); }
  function send(text, opts = {}) {
    const c = conv(state.current); if (!c || !text.trim()) return;
    const by = ME_NAME; const now = Date.now();
    if (c.windowClosed) { c.messages.push({ dir: 'out', at: now, by, text, state: 'failed' }); $('#input').value = ''; autosize(); renderChat(); return; }
    let out = text;
    if (c.lang !== 'zh' && hasCJK(text) && !opts.zh) { const d = c.drafts.find(x => x.zh === text.trim()); if (d) out = d.text; }
    const m = { dir: 'out', at: now, by, text: out, state: 'pending' };
    c.messages.push(m); c.botActive = false;
    if (c.sos && !c.sos.repliedAt) { c.sos.repliedAt = now; c.sos.claimedBy = ME; }
    state.sentline[c.id] = now;
    $('#input').value = ''; autosize(); renderChat();
    setTimeout(() => { m.state = 'read'; if (state.current === c.id) renderChat(); }, 1200);
  }
  $('#input').addEventListener('input', () => {
    autosize(); const v = $('#input').value; $('#send').disabled = !v.trim();
    if (v.startsWith('/')) return openDesk(v, true);   // ChatDaddy 习惯：打 /fcc 直接弹话术
    closeSlash(false);
    const c = conv(state.current); if (c && c.lang !== 'zh') renderChat();
  });
  $('#composer').addEventListener('submit', e => { e.preventDefault(); send($('#input').value); });
  $('#voice').addEventListener('click', () => toast('语音转文字：接入后按住说话'));
  $('#back').addEventListener('click', () => { state.queue = null; closeChat(); });
  $('#above').addEventListener('click', e => {
    const c = conv(state.current); if (!c) return;
    if (e.target.closest('#gate')) { c.botActive = false; c.sos && (c.sos.claimedBy = ME, c.sos.claimedAt = Date.now()); renderChat(); toast('Bot 已停，你来回'); setTimeout(() => $('#input').focus(), 100); return; }
    const d = e.target.closest('[data-draft]'); if (d) { const dr = c.drafts[+d.dataset.draft]; return insert(dr.zh || dr.text); }
    if (e.target.closest('#moreDrafts')) { state.draftOffset[c.id] = ((state.draftOffset[c.id] || 0) + 2) % Math.max(1, c.drafts.length); return renderChat(); }
    if (e.target.closest('#sendZh')) return send($('#input').value, { zh: true });
    if (e.target.closest('#handback')) { c.botActive = true; state.sentline[c.id] = null; renderChat(); return toast(`已交还 ${LINES[c.line].persona}`); }
    const rc = e.target.closest('[data-rc]');
    if (rc) {
      if (rc.dataset.rc === 'ok') { c.receipt.done = true; c.warn = ''; c.messages.push({ dir: 'out', at: Date.now(), by: `${LINES[c.line].persona} · Bot`, text: '✅ 收到款项了！报名表和课前须知在这里 👉（示例链接）', state: 'read' }); renderChat(); return toast('已确认收款 · 报名表已发'); }
      if (rc.dataset.rc === 'no') { c.receipt.done = true; c.warn = ''; renderChat(); return toast('已标记：不是付款'); }
      if (rc.dataset.rc === 'reply') return $('#input').focus();
    }
  });
  $('#streamInner').addEventListener('click', e => {
    const c = conv(state.current); const b = e.target.closest('[data-fail]'); if (!c || !b) return;
    const k = b.dataset.fail;
    if (k === 'wa') return toast(`已打开 WhatsApp · ${c.waNumber}`);
    if (k === 'call') return toast('拨号：接入后直接打');
    if (k === 'tpl') { c.messages.push({ dir: 'out', at: Date.now(), by: `${LINES[c.line].persona} · 模板`, text: '唤醒模板「课程更新」已发 · 他一回复，草稿一键发出', state: 'read' }); renderChat(); return toast('模板已发'); }
    if (k === 'wait') return toast('好，等客户再发来');
  });
  $('#belowComposer').addEventListener('click', e => {
    if (!e.target.closest('#next')) return;
    const nx = nextInQueue();
    if (nx) openChat(nx.id, 'zap'); else { state.queue = null; closeChat(); toast('队列清空'); }
  });

  /* ── 更多 ── */
  const setSheet = (el, open) => { el.classList.toggle('is-open', open); $('#scrim').classList.toggle('is-open', open); };
  $('#more').addEventListener('click', () => { $('#moreTitle').textContent = conv(state.current)?.name || '更多'; setSheet($('#moreSheet'), true); });
  $('#moreSheet').addEventListener('click', e => {
    const b = e.target.closest('[data-more]'); if (!b) return; setSheet($('#moreSheet'), false);
    const c = conv(state.current); if (!c) return;
    if (b.dataset.more === 'handback') { c.botActive = true; state.sentline[c.id] = null; renderChat(); toast(`已交还 ${LINES[c.line].persona}`); }
    if (b.dataset.more === 'snooze') { if (c.sos) { c.sos.repliedAt = c.sos.repliedAt || Date.now(); } toast('明早 9:00 提醒你'); closeChat(); }
    if (b.dataset.more === 'assign') { if (c.sos) { c.sos.claimedBy = COLLEAGUE; c.sos.claimedAt = Date.now(); } toast('已转给佳佳'); closeChat(); }
  });

  /* ── 话术 ── */
  let pvTpl = null;
  function closeOverlays() { const d = $('#desk'); d.classList.remove('is-open', 'is-slash'); d.style.bottom = ''; $('#preview').classList.remove('is-open'); $('#moreSheet').classList.remove('is-open'); $('#scrim').classList.remove('is-open'); }
  function renderTpls() {
    const q = qrNormalizeQuery($('#tplSearch').value);
    let list = TEMPLATES.filter(t => (!state.tplFolder || t.folder === state.tplFolder) && qrMatches(t, q));
    list.sort((a, b) => (b.pinned - a.pinned) || (tplStats(b).uses - tplStats(a).uses) || a.name.localeCompare(b.name));
    $('#tplCount').textContent = q || state.tplFolder ? `${list.length} 条` : `${TPL_TOTAL} 条`; $('#slashCount').textContent = `${list.length} 条`;
    const top = TEMPLATES.filter(t => t.pinned).concat(TEMPLATES.filter(t => !t.pinned).sort((a, b) => tplStats(b).uses - tplStats(a).uses)).slice(0, 6);
    $('#tplRecent').innerHTML = top.map(t => `<button class="rchip" type="button" data-tpl="${t.id}">${t.pinned ? '📌 ' : ''}${esc(t.name.slice(0, 22))}</button>`).join('');
    $('#tplList').innerHTML = list.map(t => { const st = tplStats(t); const first = t.steps[0] || { text: '' };
      return `<button class="trow" type="button" data-tpl="${t.id}"><span class="th${st.images ? ' th--img' : ''}">${st.images ? ic('i-image', 'ic ic--sm') : 'Aa'}</span><div><b>${t.pinned ? '📌 ' : ''}${esc(t.name)}</b><small>${esc(t.folder)}${st.steps > 1 ? ` · ${st.steps} 步` : ''}${st.images ? ` · 🖼 ${st.images}` : ''}${st.docs ? ` · 📎 ${st.docs}` : ''} · 用过 ${st.uses} 次</small><small class="tx">${esc(first.text.split('\n')[0].slice(0, 60))}</small></div>${ic('i-chevron', 'ic ic--sm')}</button>`; }).join('')
      || `<div class="empty">没搜到「${esc(q)}」<br><small>名字、资料夹、内文都搜过了</small></div>`;
    const folders = [...new Set(TEMPLATES.map(t => t.folder))].sort();
    $('#tplFolders').innerHTML = folders.map(f => `<button class="rchip" type="button" data-folder="${esc(f)}" aria-selected="${state.tplFolder === f}">${esc(f)}</button>`).join('');
  }
  // 两种开法：✱ 按钮 = 抽屉自带搜索框；输入框打 / = 抽屉坐在输入框上面，你继续在输入框打字，焦点不动（手机键盘不跳）
  function openDesk(query, slash) {
    const d = $('#desk'); $('#tplSearch').value = query || ''; renderTpls();
    d.classList.toggle('is-slash', !!slash);
    if (slash) { d.style.bottom = ($('#composer').offsetHeight + $('#belowComposer').offsetHeight) + 'px'; d.classList.add('is-open'); return; }
    d.style.bottom = ''; setSheet(d, true);
    setTimeout(() => { const i = $('#tplSearch'); i.focus(); i.setSelectionRange(i.value.length, i.value.length); }, 320);
  }
  function closeSlash(clear) { const d = $('#desk'); if (!d.classList.contains('is-slash')) return; d.classList.remove('is-open', 'is-slash'); d.style.bottom = ''; if (clear && $('#input').value.startsWith('/')) { $('#input').value = ''; autosize(); $('#send').disabled = true; } }
  $('#openDesk').addEventListener('click', () => openDesk(''));
  $('#scrim').addEventListener('click', () => { closeOverlays(); if ($('#input').value.startsWith('/')) { $('#input').value = ''; autosize(); $('#send').disabled = true; } });
  $('#tplSearch').addEventListener('input', renderTpls);
  $('#desk').addEventListener('click', e => {
    const f = e.target.closest('[data-folder]'); if (f) { state.tplFolder = state.tplFolder === f.dataset.folder ? '' : f.dataset.folder; return renderTpls(); }
    const t = e.target.closest('[data-tpl]'); if (!t) return;
    pvTpl = TEMPLATES.find(x => x.id === t.dataset.tpl); const c = conv(state.current); const st = tplStats(pvTpl);
    $('#pvName').textContent = (pvTpl.pinned ? '📌 ' : '') + pvTpl.name + (st.steps > 1 ? ` · ${st.steps} 步` : '');
    $('#pvText').textContent = qrFill(pvTpl.steps.map(x => x.text).filter(Boolean).join('\n\n'), c);
    $('#pvThumb').hidden = !(st.images || st.docs); $('#pvThumb').innerHTML = st.docs && !st.images ? '📎' : ic('i-image', 'ic ic--lg');
    $('#pvSend').textContent = st.images || st.docs ? `发送 · ${[st.images ? `${st.images} 图` : '', st.docs ? `${st.docs} 文件` : ''].filter(Boolean).join(' + ')} + 文字` : '发送';
    $('#desk').classList.remove('is-open'); $('#preview').classList.add('is-open'); $('#scrim').classList.add('is-open');
  });
  $('#slashClose').addEventListener('click', () => { closeSlash(true); $('#input').focus(); });
  function sendTemplate(t) {
    const c = conv(state.current); if (!c) return;
    if ($('#input').value.startsWith('/')) { $('#input').value = ''; autosize(); }
    if (c.windowClosed) return send(qrFill(t.steps[0].text, c));
    // 发送顺序照 jwc-bot：每一步先图（第一张带文字当 caption）→ 文件 → 剩下的文字
    const now = Date.now(); let n = 0;
    for (const st of t.steps) {
      let pending = qrFill(st.text, c).trim();
      st.images.forEach((im, i) => { const cap = i === 0 && pending && pending.length <= 1000 ? pending : ''; c.messages.push({ dir: 'out', at: now + n++, by: ME_NAME, image: true, file: im.filename, text: cap, state: 'read' }); if (cap) pending = ''; });
      st.docs.forEach(d => c.messages.push({ dir: 'out', at: now + n++, by: ME_NAME, doc: true, file: d.filename, text: '', state: 'read' }));
      if (pending) c.messages.push({ dir: 'out', at: now + n++, by: ME_NAME, text: pending, state: 'read' });
    }
    t.uses++; c.botActive = false;
    if (c.sos && !c.sos.repliedAt) { c.sos.repliedAt = now; c.sos.claimedBy = ME; }
    state.sentline[c.id] = now; renderChat(); toast(`模版「${t.name}」已发 · ${n} 条`);
  }
  $('#pvSend').addEventListener('click', () => { const t = pvTpl; closeOverlays(); sendTemplate(t); });
  $('#pvFill').addEventListener('click', () => { const t = pvTpl; closeOverlays(); insert(qrFill(t.steps.map(x => x.text).filter(Boolean).join('\n\n'), conv(state.current))); });

  /* ── IG/FB 号码 ── */
  function openHandoff() { renderHandoff(); $('#handoff').classList.add('is-open'); }
  function renderHandoff() {
    $('#handoffList').innerHTML = HANDOFFS.map(h => `<div class="hrow${h.done ? ' is-done' : ''}"><div class="top"><span class="ava"><span>${esc(h.name[0])}</span><i>☕</i></span><div style="min-width:0"><div class="qtop"><span class="qname">${esc(h.name)} <span style="font-weight:500;color:var(--uk-muted)">${esc(h.handle)}</span></span><span class="num" style="font-size:11.5px;color:var(--uk-time)">${waitMin(h.at)} 分钟前</span></div><div style="font-size:12.5px;color:var(--uk-muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${esc(h.account)} · ${esc(h.course)}</div></div></div><p class="said">${esc(h.said)}</p><div class="acts"><button class="big" type="button" data-h="wa" data-id="${h.id}" style="min-height:44px;flex-direction:row;gap:7px">${ic('i-wa', 'ic ic--sm')}打开 WhatsApp <span class="num" style="font-weight:600;opacity:.85">${esc(h.number)}</span></button><button class="soft" type="button" data-h="done" data-id="${h.id}" style="padding:0 14px">${h.done ? '已联系 ✓' : '已联系'}</button></div></div>`).join('');
  }
  $('#handoffList').addEventListener('click', e => { const b = e.target.closest('[data-h]'); if (!b) return; const h = HANDOFFS.find(x => x.id === b.dataset.id); if (b.dataset.h === 'wa') return toast(`已打开 WhatsApp · ${h.number}`); h.done = !h.done; renderHandoff(); renderQueue(); });
  $('#backHandoff').addEventListener('click', () => $('#handoff').classList.remove('is-open'));

  /* ── 启动 ── */
  setInterval(() => { if (!$('#queue').hidden && !$('#chat').classList.contains('is-open')) renderQueue(); }, 30000);
  if (loggedIn()) { show('queue'); renderQueue(); setTimeout(() => showNotif('sharon'), 900); } else { show('login'); }
  /* ── 装成 app 提示：浏览器里开才出现；Android 直接弹安装，iPhone 教两步 ── */
  (() => {
    const standalone = (window.matchMedia && matchMedia('(display-mode: standalone)').matches) || navigator.standalone === true;
    let dismissed = false; try { dismissed = sessionStorage.getItem('sw_install_x') === '1'; } catch {}
    if (standalone || dismissed) return;
    const box = $('#install'), go = $('#installGo'), how = $('#installHow');
    const ios = /iphone|ipad|ipod/i.test(navigator.userAgent);
    if (ios) { how.textContent = /crios|fxios/i.test(navigator.userAgent) ? '用 Safari 打开这个网址，再点「分享」→「添加到主屏幕」' : '点 Safari 底部「分享」→「添加到主屏幕」'; box.hidden = false; }
    else { how.textContent = 'Chrome 右上 ⋮ →「安装应用」'; box.hidden = false; }
    let deferred = null;
    addEventListener('beforeinstallprompt', e => { e.preventDefault(); deferred = e; go.hidden = false; how.textContent = '点右边「安装」，主屏幕就有图标'; });
    go.addEventListener('click', async () => { if (!deferred) return; deferred.prompt(); const r = await deferred.userChoice; if (r && r.outcome === 'accepted') box.hidden = true; deferred = null; });
    addEventListener('appinstalled', () => { box.hidden = true; });
    $('#installX').addEventListener('click', () => { box.hidden = true; try { sessionStorage.setItem('sw_install_x', '1'); } catch {} });
  })();
  window.MiaoHui = { state, CONVS, TEMPLATES };
})();
