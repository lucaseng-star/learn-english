/* ============================================================
   秒回 —— 客户消息回复台（手机端）
   ------------------------------------------------------------
   这是可点的原型：界面、交互、状态流转都是真的，数据是示例。
   接真实渠道时只替换下面的 adapter（见 ChannelAdapter 契约），
   界面层一行不用改。

   ChannelAdapter 契约：
     list()                 → Promise<Conversation[]>   拉全部会话
     send(convId, message)  → Promise<Message>          发出一条，回来带服务端时间/状态
     setStatus(convId, s)   → Promise<void>             open | follow | done
     onMessage(cb)          → () => void                新消息推送，返回取消订阅

   可接的渠道（按可行性排）：
     WhatsApp  —— WhatsApp Business Cloud API（官方，能收能发）
     IG / FB   —— Meta Messenger Platform（官方，24 小时回复窗口）
     小红书    —— 没有私信 API。只能人工看、这里手动记；把客户导到 WhatsApp
   ============================================================ */
(() => {
  'use strict';

  /* ── 示例数据（JWC Academy 课程咨询）──────────────────────── */
  const COURSES = {
    barista: { name: '咖啡师速成班',  price: 'RM 2,880',      ptpk: true,  days: '5 天',  time: '10:00–17:00' },
    latte:   { name: '拉花进阶班',    price: 'RM 980',        ptpk: false, days: '2 天',  time: '10:00–17:00' },
    cupping: { name: '杯测与感官课',  price: 'RM 1,280',      ptpk: false, days: '2 天',  time: '10:00–17:00' },
    wine:    { name: '企业红酒品鉴',  price: 'RM 168 / 人',   ptpk: false, days: '2 小时', time: '上门' },
  };
  const CHANNELS = {
    wa:  { label: 'WhatsApp',  mark: 'W',  cls: 'ch--wa',  links: true  },
    ig:  { label: 'Instagram', mark: 'I',  cls: 'ch--ig',  links: true  },
    fb:  { label: 'Facebook',  mark: 'F',  cls: 'ch--fb',  links: true  },
    xhs: { label: '小红书',    mark: '小', cls: 'ch--xhs', links: false }, // 私信发不了链接
  };
  const LANG_NAME = { zh: '中文', en: 'English', bm: 'Bahasa Melayu' };

  // 会话：status open=待回复 / follow=跟进中（我已回，等客户）/ done=已完成
  const SAMPLE = [
    {
      id: 'c1', name: '陈美琪', channel: 'wa', course: 'barista', lang: 'zh',
      status: 'open', waitMin: 96, budget: 'RM 3,000 以内',
      source: 'Meta 广告 · 咖啡师速成班 CTA-B', firstAt: '今天 12:26', stage: '新线索',
      messages: [
        { dir: 'in',  t: '12:26', text: 'Hi 我在 FB 看到咖啡师课程的广告' },
        { dir: 'out', t: '12:26', by: 'Bot', read: true, text: '您好！感谢关注 JWC 咖啡师速成班。请问您是想转行做咖啡师，还是想自己开店呢？' },
        { dir: 'in',  t: '12:27', text: '想开店，小型的那种' },
        { dir: 'out', t: '12:27', by: 'Bot', read: true, type: 'card', course: 'barista' },
        { dir: 'in',  t: '12:31', text: '请问 PTPK 可以用吗？我没有工作证明' },
        { dir: 'in',  t: '12:34', text: '在吗' },
      ],
      drafts: [
        { why: '答疑 · 约看班',
          zh: '美琪你好，PTPK 不需要工作证明，需要的是：身份证、最高学历证书、两张照片。\n开店方向的话我建议先来校区看一次实操课（免费），周六 10 点有一场，要帮你留位吗？',
          en: "Hi Mei Qi, PTPK doesn't need proof of employment — just your IC, highest education certificate and two passport photos.\nSince you're planning to open a café, come see a live practical session first (free). There's one this Saturday at 10am — shall I reserve a spot for you?",
          bm: 'Hai Mei Qi, PTPK tidak memerlukan surat pengesahan kerja — cukup IC, sijil pendidikan tertinggi dan dua keping gambar.\nMemandangkan awak nak buka kafe, datang tengok kelas praktikal dulu (percuma). Ada sesi Sabtu ini 10 pagi — nak saya simpan tempat?' },
        { why: '先要资料',
          zh: '美琪，可以的，PTPK 看的是身份证和学历，不看工作证明。\n方便把身份证正面和最高学历证书拍给我吗？我今天帮你先预审，通过就锁 9 月班的名额。',
          en: "Mei Qi, yes you can — PTPK looks at your IC and education, not employment.\nCould you send me a photo of your IC (front) and highest certificate? I'll pre-check today and lock a September seat once it clears.",
          bm: 'Mei Qi, boleh — PTPK tengok IC dan pendidikan, bukan pekerjaan.\nBoleh hantar gambar IC (depan) dan sijil tertinggi? Saya semak dulu hari ini, lepas lulus terus kunci tempat kelas September.' },
        { why: '推名额',
          zh: '可以用 PTPK，全额 RM 2,880 都能贷，每月还款大约 RM 100。\n9 月 16 日开的班还剩 2 个位，要我先帮你留一个吗？留位不用付钱。',
          en: 'Yes, PTPK covers the full RM 2,880 — repayment is around RM 100 a month.\nThe 16 Sept intake has 2 seats left. Want me to hold one for you? No payment needed to hold.',
          bm: 'Boleh guna PTPK, penuh RM 2,880 — bayaran balik lebih kurang RM 100 sebulan.\nKelas 16 Sept tinggal 2 tempat. Nak saya simpan satu untuk awak? Simpan tempat tak perlu bayar.' },
      ],
    },
    {
      id: 'c2', name: 'Nurul Aisyah', channel: 'ig', course: 'latte', lang: 'bm',
      status: 'open', waitMin: 41, budget: '未知',
      source: 'IG 帖子 · 拉花视频', firstAt: '今天 13:21', stage: '新线索',
      messages: [
        { dir: 'in', t: '13:21', text: 'Hi, boleh tahu harga untuk latte art class? Weekend ada ke?' },
      ],
      drafts: [
        { why: '报价 · 周末班',
          bm: 'Hai Nurul! Kelas Latte Art Lanjutan RM 980, 2 hari (Sabtu & Ahad, 10 pagi–5 petang).\nSesi 13–14 Sept masih ada 3 tempat. Nak saya simpan satu untuk awak?',
          zh: 'Nurul 你好！拉花进阶班 RM 980，两天（周六日 10:00–17:00）。\n9 月 13–14 日这期还剩 3 个位，要帮你留一个吗？',
          en: 'Hi Nurul! Advanced Latte Art is RM 980 for 2 days (Sat & Sun, 10am–5pm).\nThe 13–14 Sept weekend still has 3 seats. Shall I hold one for you?' },
        { why: '先问基础',
          bm: 'Hai Nurul! Sebelum saya cadangkan kelas — awak dah pernah buat latte art, atau baru nak mula?\nKami ada kelas asas (RM 680) dan lanjutan (RM 980), supaya tak bayar lebih.',
          zh: 'Nurul 你好！先问一下：你之前有做过拉花吗，还是零基础？\n我们有基础班（RM 680）和进阶班（RM 980），选对了不多花钱。',
          en: "Hi Nurul! Quick question first — have you done latte art before, or starting fresh?\nWe run a basics class (RM 680) and an advanced one (RM 980), so you don't overpay." },
        { why: '约通话',
          bm: 'Hai Nurul, jadual & harga kelas Latte Art hujung minggu saya hantar dalam kad kursus.\nKalau nak, saya boleh call 5 minit untuk explain — bila masa sesuai?',
          zh: 'Nurul 你好，周末拉花班的时间和价格我用课程卡发你。\n如果方便，我打 5 分钟电话给你讲一下，什么时间合适？',
          en: "Hi Nurul, I'll send the weekend Latte Art schedule and price as a course card.\nHappy to explain on a 5-minute call — when suits you?" },
      ],
    },
    {
      id: 'c3', name: '林伟豪', channel: 'fb', course: 'barista', lang: 'zh',
      status: 'open', waitMin: 18, budget: '2 人',
      source: 'FB 广告 · 转行做咖啡师', firstAt: '今天 13:40', stage: '新线索',
      messages: [
        { dir: 'in',  t: '13:40', text: '你好 想问咖啡师课程' },
        { dir: 'out', t: '13:40', by: 'Bot', read: true, type: 'card', course: 'barista' },
        { dir: 'in',  t: '13:44', text: '两个人一起报名有折扣吗' },
      ],
      drafts: [
        { why: '双人价',
          zh: '伟豪你好，两人同报每人减 RM 200，即每人 RM 2,680。\n如果两位都用 PTPK，还可以各自申请全额。请问两位想上平日班还是周末班？',
          en: "Hi Wei Hao, two sign-ups together get RM 200 off each — RM 2,680 per person.\nIf you both use PTPK, each can apply for full coverage. Weekday or weekend class?",
          bm: 'Hai Wei Hao, daftar berdua dapat potongan RM 200 seorang — RM 2,680 setiap orang.\nKalau berdua guna PTPK, masing-masing boleh mohon penuh. Kelas hari biasa atau hujung minggu?' },
        { why: '先问需求',
          zh: '有的，两人同报有优惠。先问一下，两位是想一起开店，还是各自找工作？方向不同我推荐的班次不一样。',
          en: 'Yes, there is a discount for two. Quick one first — are you two planning to open a café together, or each looking for a job? The class I recommend depends on that.',
          bm: 'Ada, daftar berdua ada diskaun. Tanya dulu — korang nak buka kafe bersama, atau masing-masing cari kerja? Cadangan kelas berbeza.' },
        { why: '推试听',
          zh: '两人同报每人减 RM 200。建议两位周六一起来看一节实操课（免费），看完再决定，要帮你们留两个位吗？',
          en: 'RM 200 off each for two. I suggest you both come see a live practical session this Saturday (free) before deciding — shall I hold two seats?',
          bm: 'Potongan RM 200 seorang untuk berdua. Cadangan: datang tengok kelas praktikal Sabtu ini (percuma) sebelum putuskan — nak saya simpan dua tempat?' },
      ],
    },
    {
      id: 'c4', name: '小红薯6621', channel: 'xhs', course: 'wine', lang: 'zh',
      status: 'open', waitMin: 7, budget: '20 人',
      source: '小红书 · 企业品鉴帖', firstAt: '今天 13:55', stage: '企业线索',
      messages: [
        { dir: 'in', t: '13:55', text: '看到你们企业品鉴的贴，我们公司 20 人，能来公司办吗' },
      ],
      drafts: [
        { why: '可以 · 报价',
          zh: '可以的，企业品鉴我们上门办：20 人 RM 168/人，含 5 款酒、品鉴杯、讲师 2 小时。\n请问贵司在哪一区？我发一份报价单给您。',
          en: "Yes — we run corporate tastings on-site: RM 168 per person for 20 pax, including 5 wines, glassware and a 2-hour sommelier session.\nWhich area is your office in? I'll send a quotation.",
          bm: 'Boleh — sesi wine tasting korporat kami buat di pejabat anda: RM 168 seorang untuk 20 pax, termasuk 5 jenis wain, gelas dan sommelier 2 jam.\nPejabat di kawasan mana? Saya hantar sebut harga.' },
        { why: '导到 WhatsApp',
          zh: '可以上门办的。小红书私信发不了报价单和链接，方便留个 WhatsApp 吗？我把报价单和往期活动照片发过去。',
          en: "Yes, we can host it at your office. Xiaohongshu DMs don't allow files or links — could you share a WhatsApp number? I'll send the quotation and photos from past sessions.",
          bm: 'Boleh buat di pejabat anda. DM Xiaohongshu tak boleh hantar fail atau link — boleh kongsi nombor WhatsApp? Saya hantar sebut harga dan gambar sesi lepas.' },
        { why: '要时间',
          zh: '可以的！请问大概想安排在哪个月？工作日晚上还是周五下午？确定时间我就能锁讲师和酒。',
          en: 'Yes! Roughly which month are you thinking, and weekday evening or Friday afternoon? Once we fix a date I can lock the sommelier and wines.',
          bm: 'Boleh! Lebih kurang bulan bila, dan malam hari biasa atau petang Jumaat? Bila tarikh ditetapkan saya boleh kunci sommelier dan wain.' },
      ],
    },
    {
      id: 'c5', name: 'Kelvin Tan', channel: 'wa', course: 'cupping', lang: 'zh',
      status: 'open', waitMin: 3, budget: '老学员',
      source: '老学员推荐', firstAt: '昨天 16:10', stage: '待成交',
      messages: [
        { dir: 'in',  t: '昨天', text: '下期杯测课什么时候' },
        { dir: 'out', t: '13:40', by: '你', read: true, text: 'Kelvin，杯测课下一期 9 月 20–21 日，RM 1,280，老学员价 RM 1,080。' },
        { dir: 'in',  t: '13:58', text: 'ok 我看看 时间表发我' },
      ],
      drafts: [
        { why: '发课表',
          zh: '好的 Kelvin，课表用 PDF 发你。两天都是 10:00–17:00，第二天下午是产地盲测。\n名额还有 4 个，你定了跟我说一声就行。',
          en: "Sure Kelvin, sending the schedule as a PDF. Both days run 10am–5pm; day two afternoon is the origin blind cupping.\n4 seats left — just tell me when you've decided.",
          bm: 'Baik Kelvin, jadual saya hantar dalam PDF. Dua-dua hari 10 pagi–5 petang; petang hari kedua ialah blind cupping ikut origin.\nTinggal 4 tempat — bagitahu saja bila dah decide.' },
        { why: '锁名额',
          zh: 'Kelvin，课表这就发。老学员价 RM 1,080 只到这周日，我先帮你 hold 一个位到周日晚，可以吗？',
          en: "Kelvin, schedule coming right up. The alumni price RM 1,080 is valid till this Sunday — I'll hold a seat for you till Sunday night, okay?",
          bm: 'Kelvin, jadual saya hantar sekarang. Harga alumni RM 1,080 sah sampai Ahad ini — saya simpan satu tempat sampai Ahad malam, ok?' },
      ],
    },
    {
      id: 'c6', name: '黄雅琳', channel: 'wa', course: 'barista', lang: 'zh',
      status: 'follow', waitMin: 0, remind: '明早 9:00', budget: 'RM 2,880（已报价）',
      source: 'Meta 广告 · 咖啡师速成班 CTA-A', firstAt: '昨天 11:02', stage: '已报价',
      messages: [
        { dir: 'in',  t: '昨天', text: '学费多少？可以分期吗' },
        { dir: 'out', t: '昨天', by: '你', read: true, text: '雅琳你好，咖啡师速成班 RM 2,880，可以分 3 期无利息，也可以用 PTPK 全额。' },
        { dir: 'in',  t: '昨天', text: '我跟老公商量一下' },
        { dir: 'out', t: '昨天', by: '你', read: true, text: '好的，你先考虑，我明天再跟你确认一次，名额帮你先 hold 到明晚。' },
      ],
      drafts: [
        { why: '跟进',
          zh: '雅琳早，昨天说帮你 hold 的位还在。今晚前定的话我把开课须知发你，有什么顾虑也可以直接问我。',
          en: "Morning Ya Lin — the seat I held for you is still yours. If you decide by tonight I'll send the pre-class notes; any concerns, just ask.",
          bm: 'Selamat pagi Ya Lin — tempat yang saya simpan masih ada. Kalau decide sebelum malam ini saya hantar nota pra-kelas; ada apa-apa keraguan tanya saja.' },
      ],
    },
    {
      id: 'c7', name: 'Farah', channel: 'ig', course: 'latte', lang: 'bm',
      status: 'done', waitMin: 0, budget: 'RM 980（已付）',
      source: 'IG 广告 · 拉花周末班', firstAt: '周一', stage: '已成交',
      messages: [
        { dir: 'in',  t: '周一', text: 'Nak daftar kelas latte art weekend' },
        { dir: 'out', t: '周一', by: '你', read: true, text: 'Baik Farah, ini link pendaftaran. Lepas bayar hantar resit ya.' },
        { dir: 'in',  t: '周一', text: 'Dah daftar, thank you!' },
      ],
      drafts: [],
    },
  ];

  // 快捷话术：{name} {course} {price} 在插入时替换
  const TEMPLATES = [
    { group: '价格与付款', items: [
      { k: '报价',   zh: '{name} 你好，{course} 学费 {price}，含教材和考核证书。', en: 'Hi {name}, the {course} is {price}, including materials and the assessment certificate.', bm: 'Hai {name}, yuran {course} ialah {price}, termasuk bahan dan sijil penilaian.' },
      { k: '分期',   zh: '可以分 3 期，无利息：报名付 50%，开课付 30%，结课付 20%。', en: 'You can pay in 3 interest-free instalments: 50% at sign-up, 30% on day one, 20% at completion.', bm: 'Boleh bayar 3 ansuran tanpa faedah: 50% masa daftar, 30% hari pertama, 20% selepas tamat.' },
      { k: 'PTPK',   zh: 'PTPK 可申请全额贷款，需要身份证 + 最高学历证书 + 两张照片，我们帮你办。', en: 'PTPK can cover the full fee. You need your IC, highest certificate and two photos — we handle the application.', bm: 'PTPK boleh tanggung yuran penuh. Perlu IC, sijil tertinggi dan dua gambar — kami uruskan permohonan.' },
      { k: '押金',   zh: '留位押金 RM 300，开课当天抵扣学费，开课前 7 天可全额退。', en: 'A RM 300 deposit holds your seat, deducted from the fee on day one; fully refundable up to 7 days before class.', bm: 'Deposit RM 300 untuk simpan tempat, ditolak dari yuran pada hari pertama; boleh refund penuh sehingga 7 hari sebelum kelas.' },
    ]},
    { group: '课程安排', items: [
      { k: '开课时间', zh: '{course} 下一期开课在 9 月 16 日（周一），平日班 10:00–17:00。', en: 'The next {course} intake starts Monday 16 Sept, weekday class 10am–5pm.', bm: 'Kelas {course} seterusnya bermula Isnin 16 Sept, kelas hari biasa 10 pagi–5 petang.' },
      { k: '周末班',   zh: '周末班是连续两个周末（周六日），时间一样 10:00–17:00。', en: 'The weekend class runs over two consecutive weekends (Sat & Sun), same hours 10am–5pm.', bm: 'Kelas hujung minggu berjalan dua hujung minggu berturut (Sabtu & Ahad), waktu sama 10 pagi–5 petang.' },
      { k: '名额',     zh: '这一期还剩 2 个位，报满就要等下一期（10 月）。', en: 'Only 2 seats left this intake — after that it is the October intake.', bm: 'Tinggal 2 tempat sahaja sesi ini — selepas itu sesi Oktober.' },
    ]},
    { group: '到访', items: [
      { k: '校区地址', zh: '校区在 Bukit Jalil，停车免费 3 小时，定位我发你。', en: 'The campus is in Bukit Jalil with 3 hours free parking — sending you the location pin.', bm: 'Kampus di Bukit Jalil, parking percuma 3 jam — saya hantar lokasi.' },
      { k: '约试听',   zh: '欢迎来看一节实操课（免费），周六 10:00 有一场，要帮你留位吗？', en: "You're welcome to sit in on a live practical session (free). There's one Saturday 10am — shall I hold a spot?", bm: 'Jemput datang tengok kelas praktikal (percuma). Ada sesi Sabtu 10 pagi — nak saya simpan tempat?' },
    ]},
    { group: '收尾', items: [
      { k: '稍后跟进', zh: '好的，你先考虑，我明天再跟你确认一次，名额帮你先 hold 到明晚。', en: "Sure, take your time. I'll check back tomorrow and hold the seat for you till tomorrow night.", bm: 'Baik, fikir dulu. Saya follow up esok dan simpan tempat sampai esok malam.' },
      { k: '感谢',     zh: '谢谢 {name}！报名确认后我会把课前须知和群链接发给你。', en: "Thanks {name}! Once your registration is confirmed I'll send the pre-class notes and group link.", bm: 'Terima kasih {name}! Selepas pendaftaran disahkan saya hantar nota pra-kelas dan link kumpulan.' },
      { k: '留 WhatsApp', zh: '这里发不了链接和文件，方便留个 WhatsApp 吗？我把资料发过去。', en: "I can't send links or files here — could you share a WhatsApp number? I'll send the details there.", bm: 'Di sini tak boleh hantar link atau fail — boleh kongsi nombor WhatsApp? Saya hantar butiran di sana.' },
    ]},
  ];

  const ASSETS = [
    { k: 'card',  icon: 'i-doc',  label: '课程报价卡', needsLinks: false },
    { k: 'pin',   icon: 'i-pin',  label: '校区位置',   needsLinks: true  },
    { k: 'link',  icon: 'i-link', label: '报名链接',   needsLinks: true  },
    { k: 'pdf',   icon: 'i-clip', label: '课程表 PDF', needsLinks: true  },
  ];

  /* ── Adapter（原型：内存版）───────────────────────────────── */
  const MockAdapter = {
    _convs: SAMPLE.map(c => ({ ...c, messages: c.messages.slice() })),
    _subs: [],
    async list() { return this._convs; },
    async send(id, msg) {
      const c = this._convs.find(x => x.id === id);
      const m = { ...msg, dir: 'out', by: '你', t: nowHM(), read: false };
      c.messages.push(m);
      setTimeout(() => { m.read = true; this._subs.forEach(cb => cb({ type: 'read', id })); }, 1400);
      return m;
    },
    async setStatus(id, status, extra = {}) {
      const c = this._convs.find(x => x.id === id);
      Object.assign(c, { status }, extra);
    },
    onMessage(cb) { this._subs.push(cb); return () => { this._subs = this._subs.filter(f => f !== cb); }; },
  };
  const adapter = MockAdapter;

  /* ── 状态 ─────────────────────────────────────────────────── */
  const state = {
    convs: [],
    filter: 'open',
    lang: 'zh',
    deskTab: 'drafts',
    current: null,          // 当前会话 id
    queue: null,            // { ids: [], i: 0 } 清队列模式
    doneToday: 14,
  };

  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const el = {
    qlist: $('#qlist'), statOpen: $('#stat-open'), statDone: $('#stat-done'), statWorst: $('#stat-worst'),
    pulse: $('#pulse'), queueN: $('#queueN'), startQueue: $('#startQueue'),
    chat: $('#chat'), back: $('#back'), chatAva: $('#chatAva'), chatName: $('#chatName'), chatSub: $('#chatSub'),
    ctx: $('#ctx'), ctxLine: $('#ctxLine'), ctxGrid: $('#ctxGrid'), stream: $('#stream'),
    composer: $('#composer'), input: $('#input'), send: $('#send'), voice: $('#voice'), openDesk: $('#openDesk'),
    desk: $('#desk'), deskBody: $('#deskBody'), scrim: $('#scrim'),
    qbar: $('#qbar'), qbarText: $('#qbarText'), qbarFill: $('#qbarFill'), qbarSkip: $('#qbarSkip'), qbarExit: $('#qbarExit'),
    snoozeSheet: $('#snoozeSheet'), moreSheet: $('#moreSheet'), moreTitle: $('#moreTitle'),
    actSnooze: $('#actSnooze'), actDone: $('#actDone'), actTag: $('#actTag'), more: $('#more'),
    toast: $('#toast'), toastText: $('#toastText'),
  };

  /* ── 工具 ─────────────────────────────────────────────────── */
  function nowHM() { const d = new Date(); return `${String(d.getHours()).padStart(2,'0')}:${String(d.getMinutes()).padStart(2,'0')}`; }
  function esc(s) { return String(s).replace(/[&<>"']/g, ch => ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[ch])); }
  function icon(id, cls = 'ic') { return `<svg class="${cls}" aria-hidden="true"><use href="#${id}"/></svg>`; }
  function conv(id) { return state.convs.find(c => c.id === id); }
  function initial(name) { return /^[A-Za-z]/.test(name) ? name[0].toUpperCase() : name.replace(/^小红薯/, '薯')[0]; }
  function waitLabel(c) {
    if (c.status === 'done') return { cls: 'wait--cool', text: '已完成' };
    if (c.status === 'follow') return { cls: 'wait--cool', text: c.remind ? `提醒 ${c.remind}` : '等客户' };
    const m = c.waitMin;
    const cls = m >= 60 ? 'wait--hot' : m >= 15 ? 'wait--warm' : 'wait--cool';
    const text = m >= 60 ? `等 ${Math.floor(m/60)} 小时 ${m%60} 分` : `等 ${m} 分`;
    return { cls, text };
  }
  function fill(tpl, c) {
    const course = COURSES[c.course];
    return tpl.replace(/\{name\}/g, c.name).replace(/\{course\}/g, course.name).replace(/\{price\}/g, course.price);
  }
  function openConvs() { return state.convs.filter(c => c.status === 'open').sort((a, b) => b.waitMin - a.waitMin); }
  function lastIn(c) { const m = c.messages.slice().reverse().find(x => x.dir === 'in'); return m ? m.text : ''; }

  let toastTimer;
  function toast(text) {
    el.toastText.textContent = text;
    el.toast.classList.add('is-on');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => el.toast.classList.remove('is-on'), 1800);
  }

  /* ── 渲染：队列页 ─────────────────────────────────────────── */
  function renderStats() {
    const open = openConvs();
    const worst = open.length ? open[0].waitMin : 0;
    el.statOpen.textContent = open.length;
    el.statDone.textContent = state.doneToday;
    el.statWorst.textContent = worst;
    el.pulse.lastElementChild.classList.toggle('is-hot', worst >= 60);
    el.queueN.textContent = `· ${open.length} 条`;
    el.startQueue.disabled = open.length === 0;
    $$('[data-count]').forEach(b => {
      const f = b.dataset.count;
      b.textContent = f === 'all' ? state.convs.length : state.convs.filter(c => c.status === f).length;
    });
  }

  function renderList() {
    const f = state.filter;
    let rows = f === 'all' ? state.convs.slice() : state.convs.filter(c => c.status === f);
    // 待回复按等待时长降序（最久没回的在最上面）；其它按原顺序
    if (f === 'open' || f === 'all') rows.sort((a, b) => (b.status === 'open') - (a.status === 'open') || b.waitMin - a.waitMin);
    if (!rows.length) {
      const copy = { open: ['待回清零', '没有客户在等你。'], follow: ['没有跟进中的会话', '回过的会话会在这里等客户回音。'], done: ['还没有完成的会话', '标记完成的会话会收在这里。'], all: ['没有会话', '接入渠道后这里会出现客户消息。'] }[f];
      el.qlist.innerHTML = `<li class="empty"><strong>${copy[0]}</strong><p>${copy[1]}</p></li>`;
      return;
    }
    el.qlist.innerHTML = rows.map(c => {
      const ch = CHANNELS[c.channel]; const w = waitLabel(c); const course = COURSES[c.course];
      return `<li class="qrow ${c.status === 'open' ? 'is-unread' : ''}" data-id="${c.id}">
        <span class="ava"><span class="ava-i" aria-hidden="true">${esc(initial(c.name))}</span><span class="ch ${ch.cls}" title="${ch.label}">${ch.mark}</span></span>
        <button class="qmain" type="button" data-open="${c.id}">
          <div class="qtop"><span class="qname">${esc(c.name)}</span><span class="wait ${w.cls}">${esc(w.text)}</span></div>
          <p class="qsnip">${esc(lastIn(c))}</p>
          <div class="qmeta"><span class="tag tag--blue">${esc(course.name)}</span><span class="tag tag--gray">${esc(c.source)}</span></div>
        </button>
        ${c.status === 'open' ? `<button class="zap" type="button" data-zap="${c.id}" aria-label="快速回复 ${esc(c.name)}">${icon('i-bolt')}</button>` : '<span></span>'}
      </li>`;
    }).join('');
  }

  /* ── 渲染：会话页 ─────────────────────────────────────────── */
  function renderHead(c) {
    const ch = CHANNELS[c.channel];
    el.chatAva.innerHTML = `<span class="ava-i" aria-hidden="true">${esc(initial(c.name))}</span><span class="ch ${ch.cls}">${ch.mark}</span>`;
    el.chatName.textContent = c.name;
    el.chatSub.textContent = `${ch.label} · ${LANG_NAME[c.lang]} · ${c.stage}`;
    const course = COURSES[c.course];
    el.ctxLine.textContent = `${c.source.split(' · ')[0]} · ${course.name} · ${c.budget}`;
    el.ctxGrid.innerHTML = `
      <div class="wide"><dt>来源</dt><dd>${esc(c.source)}</dd></div>
      <div><dt>咨询课程</dt><dd>${esc(course.name)}</dd></div>
      <div><dt>学费</dt><dd class="num">${esc(course.price)}${course.ptpk ? ' · PTPK 可' : ''}</dd></div>
      <div><dt>预算 / 人数</dt><dd>${esc(c.budget)}</dd></div>
      <div><dt>首次咨询</dt><dd>${esc(c.firstAt)}</dd></div>
      <div><dt>语言</dt><dd>${LANG_NAME[c.lang]}</dd></div>
      <div><dt>阶段</dt><dd>${esc(c.stage)}</dd></div>`;
    el.ctx.open = false;
  }

  function waveSvg() {
    let bars = '';
    for (let i = 0; i < 34; i++) {
      const h = 4 + Math.round(Math.abs(Math.sin(i * 1.7) * 10 + Math.cos(i * .9) * 5));
      bars += `<rect x="${i * 5.2}" y="${11 - h/2}" width="2.6" height="${h}" rx="1.3" fill="currentColor"/>`;
    }
    return `<svg viewBox="0 0 178 22" style="color:var(--uk-time)">${bars}</svg>`;
  }

  function bubble(m) {
    const meta = `<span class="meta num">${esc(m.t)}${m.dir === 'out' ? icon('i-check2', 'ic tick') : ''}</span>`;
    const by = m.dir === 'out' && m.by === 'Bot' ? '<span class="by">Bot 自动回复</span>' : '';
    if (m.type === 'card') {
      const k = COURSES[m.course];
      return `<div class="msg ${m.dir}"><div class="bubble card">${by}
        <div class="card-in"><svg aria-hidden="true"><use href="#pic-course"/></svg>
          <div class="card-b"><h4>${esc(k.name)}</h4><p class="price num">${esc(k.price)}</p>
          <p class="fine">${esc(k.days)} · ${esc(k.time)}${k.ptpk ? ' · PTPK 可申请' : ''}</p></div></div>
        <span class="cta-link" role="link" tabindex="0">查看课程详情</span>${meta}</div></div>`;
    }
    if (m.type === 'voice') {
      return `<div class="msg ${m.dir}"><div class="bubble voice"><button class="play" type="button" aria-label="播放语音">${icon('i-play')}</button><span class="wave">${waveSvg()}</span><span class="dur num">0:${String(m.sec).padStart(2,'0')}</span>${meta}</div></div>`;
    }
    return `<div class="msg ${m.dir}"><div class="bubble">${by}<p>${esc(m.text)}</p>${meta}</div></div>`;
  }

  function renderStream(c) {
    el.stream.innerHTML = `<span class="daysep">今天</span>` + c.messages.map(bubble).join('');
    el.stream.scrollTop = el.stream.scrollHeight;
  }

  /* ── 渲染：回复台 ─────────────────────────────────────────── */
  function renderDesk() {
    const c = conv(state.current); if (!c) return;
    $$('.desktab').forEach(t => t.setAttribute('aria-selected', String(t.dataset.tab === state.deskTab)));
    $$('.langsw button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.lang === state.lang)));
    const L = state.lang;
    if (state.deskTab === 'drafts') {
      const drafts = c.drafts.length ? c.drafts : [{ why: '通用', zh: fill(TEMPLATES[0].items[0].zh, c), en: fill(TEMPLATES[0].items[0].en, c), bm: fill(TEMPLATES[0].items[0].bm, c) }];
      el.deskBody.innerHTML = `
        <p class="hint">${icon('i-info', 'ic ic--sm')}<span>草稿根据客户最后一句和课程资料生成。点一条填进输入框，改完再发 —— AI 不会替你发出去。</span></p>
        ${drafts.map((d, i) => `<button class="draft" type="button" data-draft="${i}">
          <div class="dhead"><span class="why">${esc(d.why)}</span><span class="len num">${d[L].length} 字符</span></div>
          <p>${esc(d[L])}</p></button>`).join('')}`;
    } else if (state.deskTab === 'tmpls') {
      el.deskBody.innerHTML = TEMPLATES.map((g, gi) => `<div class="grp"><h4>${esc(g.group)}</h4><div class="tmpls">
        ${g.items.map((t, ti) => `<button class="tmpl" type="button" data-tmpl="${gi}.${ti}" title="${esc(fill(t[L], c))}">${esc(t.k)}</button>`).join('')}
      </div></div>`).join('');
    } else {
      const ch = CHANNELS[c.channel];
      el.deskBody.innerHTML = `
        ${ch.links ? '' : `<p class="hint">${icon('i-info', 'ic ic--sm')}<span>${esc(ch.label)} 私信发不了链接和文件。先把客户导到 WhatsApp，再发这些。</span></p>`}
        <div class="assets">${ASSETS.map(a => `<button class="asset" type="button" data-asset="${a.k}" ${a.needsLinks && !ch.links ? 'disabled style="opacity:.45"' : ''}>${icon(a.icon)}<span>${esc(a.label)}</span></button>`).join('')}</div>`;
    }
  }

  function setDesk(open) {
    el.desk.classList.toggle('is-open', open);
    el.scrim.classList.toggle('is-open', open);
    el.openDesk.setAttribute('aria-expanded', String(open));
    if (open) renderDesk();
  }
  function setSheet(sheet, open) { sheet.classList.toggle('is-open', open); el.scrim.classList.toggle('is-open', open); }
  function closeOverlays() { setDesk(false); setSheet(el.snoozeSheet, false); setSheet(el.moreSheet, false); el.scrim.classList.remove('is-open'); }

  /* ── 导航 ─────────────────────────────────────────────────── */
  function openChat(id, { desk = false } = {}) {
    const c = conv(id); if (!c) return;
    state.current = id;
    state.lang = c.lang;                     // 跟客户的语言走
    renderHead(c); renderStream(c);
    el.input.value = ''; autosize(); el.send.disabled = true;
    el.chat.classList.add('is-open');
    renderQbar();
    closeOverlays();
    if (desk) setTimeout(() => setDesk(true), 260);
    try { if (window === window.top && !history.state?.chat) history.pushState({ chat: id }, ''); } catch (_) {}
  }
  function closeChat() {
    el.chat.classList.remove('is-open');
    closeOverlays();
    state.current = null;
    renderStats(); renderList();
  }

  /* ── 清队列模式 ───────────────────────────────────────────── */
  function startQueue() {
    const ids = openConvs().map(c => c.id);
    if (!ids.length) return;
    state.queue = { total: ids.length, remaining: ids.slice(), done: 0, skipStreak: 0 };
    openChat(ids[0], { desk: true });
  }
  function renderQbar() {
    const q = state.queue;
    el.qbar.hidden = !q;
    if (!q) return;
    el.qbarText.textContent = `${q.done + 1} / ${q.total}`;
    el.qbarFill.style.width = `${Math.round(q.done / q.total * 100)}%`;
  }
  // 回完/跟进/完成 → 下一条；跳过 → 放到队尾，连续跳过一整轮就结束
  function queueNext({ skipped = false } = {}) {
    const q = state.queue; if (!q) return;
    if (skipped) { q.remaining.push(q.remaining.shift()); q.skipStreak++; }
    else { q.remaining.shift(); q.done++; q.skipStreak = 0; }
    if (!q.remaining.length || q.skipStreak >= q.remaining.length) {
      const { done, total, remaining } = q;
      state.queue = null;
      closeChat();
      toast(done === total ? `队列清空 · 回了 ${done} 条` : `回了 ${done} 条 · 跳过 ${remaining.length} 条`);
      return;
    }
    openChat(q.remaining[0], { desk: true });
  }
  function exitQueue() { state.queue = null; closeChat(); }

  /* ── 输入与发送 ───────────────────────────────────────────── */
  function autosize() {
    el.input.style.height = 'auto';
    el.input.style.height = Math.min(el.input.scrollHeight, 132) + 'px';
  }
  function insertText(text) {
    el.input.value = text;
    autosize(); el.send.disabled = !text.trim();
    setDesk(false);
    el.input.focus();
    el.input.setSelectionRange(text.length, text.length);
  }
  async function sendMessage(msg) {
    const c = conv(state.current); if (!c) return;
    const wasOpen = c.status === 'open';
    await adapter.send(c.id, msg);
    if (wasOpen) { await adapter.setStatus(c.id, 'follow', { remind: null, waitMin: 0 }); state.doneToday++; }
    renderStream(c);
    el.input.value = ''; autosize(); el.send.disabled = true;
    if (state.queue) {
      toast('已发送 · 下一条');
      setTimeout(() => queueNext(), 900);
    } else {
      toast(wasOpen ? '已发送 · 移到「跟进中」' : '已发送');
    }
  }

  /* ── 事件 ─────────────────────────────────────────────────── */
  $$('.chip').forEach(ch => ch.addEventListener('click', () => {
    state.filter = ch.dataset.filter;
    $$('.chip').forEach(x => x.setAttribute('aria-selected', String(x === ch)));
    renderList();
  }));
  el.qlist.addEventListener('click', e => {
    const open = e.target.closest('[data-open]'); if (open) return openChat(open.dataset.open);
    const zap = e.target.closest('[data-zap]');   if (zap)  return openChat(zap.dataset.zap, { desk: true });
  });
  el.startQueue.addEventListener('click', startQueue);
  el.back.addEventListener('click', () => state.queue ? exitQueue() : closeChat());
  el.qbarSkip.addEventListener('click', () => queueNext({ skipped: true }));
  el.qbarExit.addEventListener('click', exitQueue);
  window.addEventListener('popstate', () => { if (el.chat.classList.contains('is-open')) closeChat(); });

  el.openDesk.addEventListener('click', () => setDesk(!el.desk.classList.contains('is-open')));
  el.scrim.addEventListener('click', closeOverlays);
  $$('.desktab').forEach(t => t.addEventListener('click', () => { state.deskTab = t.dataset.tab; renderDesk(); }));
  $$('.langsw button').forEach(b => b.addEventListener('click', () => { state.lang = b.dataset.lang; renderDesk(); }));
  el.deskBody.addEventListener('click', e => {
    const c = conv(state.current); if (!c) return;
    const d = e.target.closest('[data-draft]');
    if (d) { const drafts = c.drafts.length ? c.drafts : null; const text = drafts ? drafts[+d.dataset.draft][state.lang] : fill(TEMPLATES[0].items[0][state.lang], c); return insertText(text); }
    const t = e.target.closest('[data-tmpl]');
    if (t) { const [gi, ti] = t.dataset.tmpl.split('.').map(Number); const text = fill(TEMPLATES[gi].items[ti][state.lang], c); const cur = el.input.value.trim(); return insertText(cur ? cur + '\n' + text : text); }
    const a = e.target.closest('[data-asset]');
    if (a && !a.disabled) {
      const k = a.dataset.asset;
      if (k === 'card') return sendMessage({ type: 'card', course: c.course });
      const text = { pin: '📍 JWC Academy · Bukit Jalil 校区（定位已发送）', link: '报名链接：jwc.academy/enrol（示例）', pdf: '📄 课程表.pdf' }[k];
      return sendMessage({ text });
    }
  });

  el.input.addEventListener('input', () => { autosize(); el.send.disabled = !el.input.value.trim(); });
  el.input.addEventListener('keydown', e => { if (e.key === 'Enter' && (e.metaKey || e.ctrlKey)) { e.preventDefault(); el.composer.requestSubmit(); } });
  el.composer.addEventListener('submit', e => { e.preventDefault(); const text = el.input.value.trim(); if (text) sendMessage({ text }); });

  // 语音转文字：有 Web Speech API 就真用，没有就说明白
  el.voice.addEventListener('click', () => {
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SR) return toast('这个浏览器没有语音识别，接入 Whisper 后可用');
    try {
      const c = conv(state.current);
      const r = new SR(); r.lang = { zh: 'zh-CN', en: 'en-MY', bm: 'ms-MY' }[c ? c.lang : 'zh']; r.interimResults = false;
      el.voice.classList.add('is-on'); toast('说话… 说完自动停');
      r.onresult = ev => { const t = ev.results[0][0].transcript; const cur = el.input.value.trim(); insertText(cur ? cur + ' ' + t : t); };
      r.onerror = () => toast('麦克风不可用（原型环境可能被禁）');
      r.onend = () => el.voice.classList.remove('is-on');
      r.start();
    } catch (_) { el.voice.classList.remove('is-on'); toast('麦克风不可用（原型环境可能被禁）'); }
  });

  el.actSnooze.addEventListener('click', () => setSheet(el.snoozeSheet, true));
  el.snoozeSheet.addEventListener('click', async e => {
    const b = e.target.closest('[data-snooze]'); if (!b) return;
    setSheet(el.snoozeSheet, false);
    const v = b.dataset.snooze; if (v === 'cancel') return;
    const c = conv(state.current);
    const remind = v === 'tomorrow' ? '明早 9:00' : (() => { const d = new Date(Date.now() + Number(v) * 60000); return `${String(d.getHours()).padStart(2,'0')}:${String(d.getMinutes()).padStart(2,'0')}`; })();
    await adapter.setStatus(c.id, 'follow', { remind, waitMin: 0 });
    toast(`${remind} 提醒你回 ${c.name}`);
    state.queue ? queueNext() : closeChat();
  });
  el.actDone.addEventListener('click', async () => {
    const c = conv(state.current);
    await adapter.setStatus(c.id, 'done', { stage: '已成交', remind: null, waitMin: 0 });
    toast(`${c.name} 已完成`);
    state.queue ? queueNext() : closeChat();
  });
  el.actTag.addEventListener('click', async () => {
    const c = conv(state.current);
    const next = c.stage === '高意向' ? '新线索' : '高意向';
    await adapter.setStatus(c.id, c.status, { stage: next });
    renderHead(c); toast(next === '高意向' ? '已标「高意向」' : '已取消「高意向」');
  });
  el.more.addEventListener('click', () => { el.moreTitle.textContent = conv(state.current)?.name || '更多操作'; setSheet(el.moreSheet, true); });
  el.moreSheet.addEventListener('click', async e => {
    const b = e.target.closest('[data-more]'); if (!b) return;
    setSheet(el.moreSheet, false);
    const c = conv(state.current); const v = b.dataset.more;
    if (v === 'call')   return toast(`拨号：${CHANNELS[c.channel].label} 号码接入后可用`);
    if (v === 'assign') return toast('转给同事：多人版再做');
    if (v === 'mute')   { await adapter.setStatus(c.id, 'done', { stage: '无效线索', waitMin: 0 }); toast('已标为无效线索'); return state.queue ? queueNext() : closeChat(); }
  });

  // 每分钟：没回的会话等待 +1，列表和顶部数字跟着动
  setInterval(() => {
    state.convs.forEach(c => { if (c.status === 'open') c.waitMin++; });
    if (!el.chat.classList.contains('is-open')) { renderStats(); renderList(); }
  }, 60000);

  /* ── 启动 ─────────────────────────────────────────────────── */
  (async () => {
    state.convs = await adapter.list();
    adapter.onMessage(ev => { if (ev.type === 'read' && state.current === ev.id) renderStream(conv(ev.id)); });
    renderStats(); renderList();
  })();

  window.MiaoHui = { state, adapter, COURSES, TEMPLATES };
})();
