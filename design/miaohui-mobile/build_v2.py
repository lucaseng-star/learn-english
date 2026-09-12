# v2 —— 照十条改。复用 v1 的 token / 小组件（从 gen_design.py 前半段取），v1 画板改名放到第二页存档。
import json, pathlib, re, sys
SCR = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(__file__).resolve().parent
src = (SCR / 'build.py').read_text()
helpers, rest = src.split('# ══════════════════════════ 1. Main —— 待回队列', 1)
ns = {}; exec(helpers, ns)
for k in ['INK','INK2','MUTED','TIME','LINE','LINE_SOFT','SURF','SURF2','CANVAS','BRAND','BRAND_SOFT','ACCENT','WARM','LINK','TICK','TAG','WAIT','STAGE',
          'ic','phone','iconbtn','tag','stage_tag','wait_pill','avatar','chip','section','primary','dock']:
    globals()[k] = ns[k]
# 会话相关共用（v1 的第二段）也要
shared, _ = rest.split('# ══════════════════════════ 2. Chat —— 会话 · 接管', 1)
shared = shared.split('# ══════════════════════════ 会话相关共用 ══════════════════════════', 1)[1]
exec(shared, ns)
for k in ['bubble_in','bubble_out','sos_marker','daysep','stream','composer','MSGS']:
    globals()[k] = ns[k]
HOT_BG, HOT_FG = WAIT['hot']; WARM_BG, WARM_FG = WAIT['warm']
def sos_marker2(bot, t):
    return (f'<div style="display:flex;justify-content:center"><div style="max-width:92%;padding:8px 12px;border-radius:10px;background:#fdecea;color:#c0392b;font-size:12.5px;font-weight:600;line-height:1.4;text-align:center">'
            f'🆘 {bot} 答不了 · 已告诉客户「5-10 分钟真人回你」<span class="num" style="font-weight:500;color:#a5443a"> · {t}</span></div></div>')
def scrim(): return '<div style="position:absolute;inset:0;background:rgba(16,24,40,.34)"></div>'

# ── 1) v1 存档：跑一遍 v1 生成器，再改名 ──
exec(src.replace("OUT = pathlib.Path(__file__).resolve().parent", "OUT = pathlib.Path('/home/user/learn-english/design/miaohui-mobile')"), {'__name__': 'v1'})
V1 = {'Main':'V1Queue','Chat':'V1Chat','Reply':'V1Drafts','Quick':'V1Quick','Sent':'V1Sent','Handoff':'V1Handoff'}
for old, new in V1.items():
    (OUT / f'{old}.dc.html').rename(OUT / f'{new}.dc.html')
v1_canvas = json.loads((OUT / 'canvas.json').read_text())

# ── v2 小组件 ──
def header2(name, line_emoji, line_label, status_html):
    return (f'<div style="display:flex;align-items:center;gap:6px;padding:8px 8px 8px 2px;border-bottom:1px solid {LINE};background:{SURF}">'
            f'<div style="width:40px;height:44px;display:flex;align-items:center;justify-content:center;color:{INK}">{ic("chevron",22,"transform:scaleX(-1);")}</div>'
            f'{avatar(name[0], line_emoji, 36)}'
            f'<div style="flex:1;min-width:0"><div style="display:flex;align-items:baseline;gap:6px"><span style="font-size:16px;font-weight:700;letter-spacing:-.015em;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{name}</span><span style="font-size:12px;color:{MUTED};white-space:nowrap">{line_emoji} {line_label}</span></div>'
            f'<div style="display:flex;gap:5px;margin-top:2px">{status_html}</div></div>'
            f'<div style="width:40px;height:44px;display:flex;align-items:center;justify-content:center;color:{INK2}">{ic("more",20)}</div></div>')
def st(text, kind='green'):
    bg,fg = TAG[kind]
    return f'<span style="padding:2px 7px;border-radius:7px;background:{bg};color:{fg};font-size:11px;font-weight:700;white-space:nowrap">{text}</span>'
def ctxline(parts, warn=None):
    w = f'<span style="color:#c0392b;font-weight:700">{warn}</span>' if warn else f'<span style="color:{TIME}">无地雷</span>'
    return (f'<div style="display:flex;align-items:center;gap:6px;padding:7px 16px;border-bottom:1px solid {LINE_SOFT};background:{SURF};font-size:12.5px;color:{INK2};white-space:nowrap;overflow:hidden">'
            + ''.join(f'<span style="font-weight:600">{p}</span><span style="color:{TIME}">·</span>' for p in parts) + w
            + f'<span style="margin-left:auto;color:{TIME}">{ic("chevron",14,"color:#9aa1ab;transform:rotate(90deg);","2")}</span></div>')
def task_card(question, wait_text, level='hot'):
    bg, fg = WAIT[level]
    return (f'<div style="margin:0 12px;padding:10px 12px;border-radius:10px;background:{SURF};border:1.5px solid {fg};box-shadow:0 1px 1px rgba(16,24,40,.09)">'
            f'<div style="display:flex;align-items:center;gap:6px;margin-bottom:4px"><span style="font-size:11px;font-weight:700;color:{fg};letter-spacing:.04em">🆘 客户在问</span><span class="num" style="margin-left:auto;padding:1px 7px;border-radius:7px;background:{bg};color:{fg};font-size:11px;font-weight:700">{wait_text}</span></div>'
            f'<div style="font-size:14.5px;font-weight:600;line-height:1.4;color:{INK}">{question}</div></div>')
def draft_card(answer, body, src='目录 ✓', width=286, lang_note=''):
    ln = f'<div style="margin-top:5px;font-size:11.5px;color:{TIME};white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{lang_note}</div>' if lang_note else ''
    return (f'<div style="flex:none;width:{width}px;padding:10px 12px;border:1px solid {LINE};border-radius:10px;background:{SURF}">'
            f'<div style="display:flex;align-items:center;gap:6px;margin-bottom:4px"><span style="flex:1;min-width:0;font-size:14px;font-weight:700;color:{INK};overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{answer}</span>{tag(src,"green")}</div>'
            f'<p style="margin:0;font-size:13px;line-height:1.42;color:{INK2};display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden">{body}</p>{ln}</div>')
def drafts_row(cards):
    head = (f'<div style="display:flex;align-items:center;gap:6px;padding:8px 12px 0;font-size:11.5px;font-weight:700;color:{MUTED};letter-spacing:.04em">{ic("asterisk",13,"color:#7b838e;")}草稿 · 只用目录里的事实'
            f'<span style="margin-left:auto;padding:4px 10px;border-radius:999px;background:{SURF2};color:{INK};font-size:12px;font-weight:700;letter-spacing:0">换一批</span></div>')
    return head + f'<div style="display:flex;gap:8px;padding:8px 12px 0;overflow:hidden">{"".join(cards)}</div>'
def composer2(text='', placeholder='以 Emily 的身份回复…', disabled=False, focused=False, right_note=''):
    if disabled:
        bar = (f'<div style="display:flex;align-items:center;gap:8px;margin:0 8px 8px;padding:10px 12px;border-radius:10px;background:#fdf3c9;color:#7a5f18;font-size:13.5px;font-weight:700">'
               f'<span style="flex:1">Bot 还在回这个对话，先停它再回</span><span style="display:flex;align-items:center;gap:4px;white-space:nowrap">🔴 停 bot 并回复 {ic("chevron",14,"","2.2")}</span></div>')
        field = f'<div style="flex:1;min-width:0;min-height:40px;padding:9px 14px;border-radius:22px;background:{SURF2};font-size:15px;line-height:1.4;color:{TIME}">{placeholder}</div>'
        return (f'<div style="padding-top:8px;border-top:1px solid {LINE};background:{SURF}">{bar}<div style="display:flex;align-items:flex-end;gap:4px;padding:0 8px 20px;opacity:.5">'
                f'<div style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;color:{INK2}">{ic("asterisk",20)}</div>{field}'
                f'<div style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;color:{INK2}">{ic("mic",20)}</div>'
                f'<div style="width:40px;height:40px;flex:none;display:flex;align-items:center;justify-content:center;border-radius:50%;background:{SURF2};color:{MUTED}">{ic("send",20)}</div></div></div>')
    cursor = f'<span style="display:inline-block;width:1.5px;height:17px;background:{INK};vertical-align:-3px;margin-left:1px"></span>' if focused else ''
    field = f'<div style="flex:1;min-width:0;min-height:40px;padding:9px 14px;border-radius:22px;background:{SURF2};font-size:15px;line-height:1.4;color:{INK if text else MUTED};{"box-shadow:0 0 0 2px rgba(46,192,106,.45);" if focused else ""}">{text or placeholder}{cursor}</div>'
    send_bg = BRAND if text else SURF2; send_fg = '#ffffff' if text else MUTED
    return (f'<div style="display:flex;align-items:flex-end;gap:4px;padding:8px 8px 20px;border-top:1px solid {LINE};background:{SURF}">'
            f'<div style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;color:{INK2}">{ic("asterisk",20)}</div>{field}'
            f'<div style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;color:{INK2}">{ic("mic",20)}</div>'
            f'<div style="width:40px;height:40px;flex:none;display:flex;align-items:center;justify-content:center;border-radius:50%;background:{send_bg};color:{send_fg}">{ic("send",20)}</div></div>')
def bubble_in_tr(text, t, tr):
    return (f'<div style="display:flex;justify-content:flex-start"><div style="position:relative;max-width:84%;padding:8px 11px 7px;border-radius:9px;border-top-left-radius:2px;background:{SURF};box-shadow:0 1px 1px rgba(16,24,40,.09);font-size:15px;line-height:1.42">'
            f'<p style="margin:0;padding-right:46px;white-space:pre-wrap">{text}</p>'
            f'<p style="margin:6px 0 0;padding-top:6px;border-top:1px dashed {LINE};font-size:13px;line-height:1.4;color:{MUTED}"><span style="font-weight:700;color:{TIME}">译</span> {tr}</p>'
            f'<span class="num" style="position:absolute;right:9px;top:8px;font-size:10.5px;color:{TIME}">{t}</span></div></div>')
def stream2(children, gap=12, pad='14px 12px 10px'):
    return f'<div style="flex:1;min-height:0;display:flex;flex-direction:column;justify-content:flex-end;gap:{gap}px;padding:{pad};overflow:hidden;background:{WARM}">' + ''.join(children) + '</div>'

# ══════════ 0. Notify —— 从通知直达（390×260）══════════
notify = (f'<div style="width:390px;height:260px;background:{CANVAS};display:flex;flex-direction:column;gap:10px;padding:16px;box-sizing:border-box;font-size:15px;line-height:1.45">'
    f'<div style="font-size:11.5px;font-weight:700;color:{MUTED};letter-spacing:.06em">推送 / TELEGRAM 通知</div>'
    f'<div style="display:flex;gap:11px;padding:12px 14px;border-radius:14px;background:{SURF};box-shadow:0 1px 2px rgba(16,24,40,.05), 0 8px 24px rgba(16,24,40,.10)">'
    f'<div style="width:38px;height:38px;flex:none;border-radius:10px;background:{BRAND};color:#ffffff;display:flex;align-items:center;justify-content:center">{ic("bolt",20,"color:#ffffff;","2")}</div>'
    f'<div style="flex:1;min-width:0"><div style="display:flex;align-items:baseline;gap:6px"><span style="font-size:14.5px;font-weight:700">🆘 Sharon 等真人 <span class="num" style="color:#c0392b">14 分</span></span><span class="num" style="margin-left:auto;font-size:11.5px;color:{TIME}">11:18</span></div>'
    f'<div style="font-size:13.5px;line-height:1.4;color:{INK2};margin-top:2px">🍷 Emily 线 · 问：刚毕业。如果中途找到全职工作可以转周末班吗？学费怎么算？</div>'
    f'<div style="font-size:12px;color:{MUTED};margin-top:4px">点开 = 认领 + 停 bot + 键盘弹出。别人先点了会显示「佳佳 已接」。</div></div></div>'
    f'<div style="display:flex;align-items:center;gap:8px;font-size:12.5px;color:{MUTED}">{ic("chevron",14,"color:#9aa1ab;transform:rotate(90deg);","2")}<span>点一下，落在右边这一屏，四步变一步</span></div></div>')
(OUT/'Notify.dc.html').write_text(ns['HEAD'] + notify + ns['TAIL'])

# ══════════ 1. Main —— 会话（从通知进来的状态）══════════
SHARON_Q = '刚毕业。如果中途找到全职工作可以转周末班吗？学费怎么算？'
main_inner = (header2('Sharon', '🍷', 'Emily 线', st('你在回','green') + st('Bot 已停','green') + st('对客户显示 Emily','gray'))
    + ctxline(['WNSM 调酒半工读', '中文', '热'])
    + stream2([daysep('今天'), bubble_in('你好 我看到调酒半工读的广告', '11:02'),
               bubble_out('哈喽 Sharon，我是 Emily 🍷 调酒半工读是 9 个月 36 堂，一周上 1 天课，其余时间在合作酒吧带薪实习。你现在是在工作，还是刚毕业？', '11:02', 'Emily · Bot'),
               bubble_in(SHARON_Q, '11:04')])
    + f'<div style="background:{WARM};padding:0 0 10px">{task_card(SHARON_Q, "等了 14 分 · 承诺 5-10")}</div>'
    + f'<div style="border-top:1px solid {LINE};background:{SURF}">'
    + drafts_row([draft_card('可以转，按剩余堂数折算', '可以的 Sharon，半工读转周末班随时可以，学费按剩余堂数折算，不会重复收。刚毕业的话建议先来看一堂实操（免费），这周六 2 点有一场，帮你留位？'),
                  draft_card('先问：边找工作还是专心学', 'Sharon 你好，想先了解一下：你是想边找工作边学，还是先专心学完 9 个月？两种情况推荐的班不一样。', '无价格')])
    + composer2('', '以 Emily 的身份回复…', focused=True) + '</div>')
(OUT/'Main.dc.html').write_text(phone(main_inner))

# ══════════ 2. Reply —— 翻译内建 + 草稿写答案（Aina · Coco 线 · BM）══════════
AINA_Q = 'Kelas Barista 1 hari tu hujung minggu ada tak? Berapa harga ya?'
AINA_TASK = '周末有场吗？多少钱？<span style="font-weight:500;color:#7b838e"> · 原文 BM</span>'
reply_inner = (header2('Aina', '☕', 'Coco 线', st('你在回','green') + st('Bot 已停','green') + st('对客户显示 Coco','gray'))
    + ctxline(['1-Day Junior Barista', 'BM · 自动翻译', '好奇'], '⚠ BM 渠道不放酒精')
    + stream2([daysep('今天'),
               bubble_in_tr('Hai, saya nampak iklan kelas barista. Untuk yang tak ada pengalaman boleh ke?', '13:52', '你好，我看到咖啡师课程的广告。没有经验的可以吗？'),
               bubble_out('Hai Aina ☕ Boleh! Kelas 1 hari ni memang untuk yang baru nak mula.', '13:52', 'Coco · Bot'),
               bubble_in_tr(AINA_Q, '13:55', '一日咖啡师课周末有场吗？多少钱？')])
    + f'<div style="background:{WARM};padding:0 0 10px">{task_card(AINA_TASK, "等了 3 分 · 承诺 5-10", "cool")}</div>'
    + f'<div style="border-top:1px solid {LINE};background:{SURF}">'
    + drafts_row([draft_card('有周末场 · 下一场 20/9 · 报价', 'Ada! Sesi hujung minggu seterusnya 20 Sept (Sabtu), 10 pagi–2 petang. Harga RM ___ termasuk bahan &amp; sijil kehadiran. Nak saya simpan tempat?', '目录 ✓', 286, '中文：有！下一场周末 9 月 20 日周六 10–2 点，RM ___ 含材料和出席证明，要留位吗？'),
                  draft_card('先问：几位一起来', 'Sebelum saya bagi harga, awak datang seorang atau berdua? Harga berdua lain sikit.', '无价格', 286, '中文：报价前先问，一个人还是两个人来？双人价不同。')])
    + f'<div style="display:flex;align-items:center;gap:8px;margin:10px 8px 0;padding:9px 12px;border-radius:10px;background:{BRAND_SOFT};font-size:12.5px;line-height:1.4;color:#1e7a45">'
    f'<span style="font-weight:700;white-space:nowrap">发出时翻成 BM ✓</span><span style="flex:1;min-width:0;color:#3c7a55;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">Ada! Sesi hujung minggu seterusnya 20 Sept, 10 pagi…</span><span style="font-weight:700;white-space:nowrap;color:{MUTED}">发中文</span></div>'
    + composer2('有的！下一场周末班 9 月 20 日周六早上 10 点，要帮你留位吗？', '', focused=True) + '</div>')
(OUT/'Reply.dc.html').write_text(phone(reply_inner))

# ══════════ 3. Gate —— 从队列进来，bot 还在回：底部一体化接管 ══════════
gate_inner = (header2('Aina', '☕', 'Coco 线', st('未认领','yellow') + st('Bot 在回','yellow') + st('对客户显示 Coco','gray'))
    + ctxline(['1-Day Junior Barista', 'BM · 自动翻译', '好奇'], '⚠ BM 渠道不放酒精')
    + stream2([daysep('今天'),
               bubble_in_tr('Hai, saya nampak iklan kelas barista. Untuk yang tak ada pengalaman boleh ke?', '13:52', '你好，我看到咖啡师课程的广告。没有经验的可以吗？'),
               bubble_out('Hai Aina ☕ Boleh! Kelas 1 hari ni memang untuk yang baru nak mula.', '13:52', 'Coco · Bot'),
               bubble_in_tr(AINA_Q, '13:55', '一日咖啡师课周末有场吗？多少钱？'), sos_marker2('Coco', '13:55')])
    + f'<div style="background:{WARM};padding:0 0 10px">{task_card(AINA_TASK, "等了 3 分 · 承诺 5-10", "cool")}</div>'
    + composer2('', '以 Coco 的身份回复…', disabled=True))
(OUT/'Gate.dc.html').write_text(phone(gate_inner))

# ══════════ 4. Sent —— 发完一行提示，不逼决定 ══════════
sent_inner = (header2('Sharon', '🍷', 'Emily 线', st('你在回','green') + st('Bot 已停','green') + st('对客户显示 Emily','gray'))
    + ctxline(['WNSM 调酒半工读', '中文', '热'])
    + stream2([daysep('今天'), bubble_in('你好 我看到调酒半工读的广告', '11:02'),
               bubble_out('哈喽 Sharon，我是 Emily 🍷 调酒半工读是 9 个月 36 堂，一周上 1 天课，其余时间在合作酒吧带薪实习。你现在是在工作，还是刚毕业？', '11:02', 'Emily · Bot'),
               bubble_in(SHARON_Q, '11:04'), sos_marker('11:04'),
               bubble_out('可以的 Sharon，半工读转周末班随时可以，学费按剩余堂数折算，不会重复收。刚毕业的话建议先来看一堂实操（免费），这周六 2 点有一场，帮你留位？', '11:19', 'Boon · 人手（客户看到的是 Emily）', 'read')])
    + f'<div style="display:flex;align-items:center;gap:8px;padding:9px 12px;border-top:1px solid {LINE};background:{SURF};font-size:13px;color:{INK2}">'
    f'{ic("check2",16,"color:#2ec06a;","2.2")}<span style="flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis"><span style="font-weight:600">已发 ✓✓ · SOS 已解决</span><span style="color:{MUTED}"> · 12 小时后 Bot 接回</span></span>'
    f'<span style="flex:none;padding:6px 10px;border-radius:999px;background:{SURF2};font-size:12.5px;font-weight:700;color:{INK};white-space:nowrap">🟢 交还</span></div>'
    + composer2('', '以 Emily 的身份回复…')
    + f'<div style="display:flex;align-items:center;gap:10px;padding:10px 16px 20px;margin-top:-12px;background:{INK};color:#ffffff">'
    f'<div style="flex:1;min-width:0"><div class="num" style="font-size:11.5px;font-weight:600;color:rgba(255,255,255,.7)">清队列 1 / 7 · 下一条</div><div style="font-size:14px;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">Aina · ☕ Coco 线 · <span class="num" style="color:#6fdc9b">等 5 分</span></div></div>'
    f'<div style="flex:none;height:40px;padding:0 14px;display:flex;align-items:center;gap:6px;border-radius:10px;background:{BRAND};color:#ffffff;font-size:14px;font-weight:700">下一条 {ic("chevron",16,"","2")}</div></div>')
(OUT/'Sent.dc.html').write_text(phone(sent_inner))

# ══════════ 5. Quick —— 话术先搜索，插入前预览 ══════════
def recent_chip(text):
    return f'<div style="flex:none;height:32px;padding:0 12px;display:flex;align-items:center;border-radius:999px;background:{SURF2};font-size:12.5px;font-weight:600;color:{INK};white-space:nowrap">{text}</div>'
def qrow(name, meta, pinned=False, on=False):
    pin = f'<span style="color:{BRAND}">📌</span> ' if pinned else ''
    bg = BRAND_SOFT if on else 'transparent'
    return (f'<div style="display:flex;align-items:center;gap:10px;padding:9px 8px;margin:0 -8px;border-radius:8px;background:{bg}">'
            f'<div style="flex:1;min-width:0"><div style="font-size:14px;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{pin}{name}</div><div class="num" style="font-size:12px;color:{MUTED}">{meta}</div></div>'
            f'{ic("chevron",16,"color:#9aa1ab;","2")}</div>')
quick_drawer = (f'<div style="position:absolute;left:0;right:0;bottom:0;height:640px;display:flex;flex-direction:column;border-radius:22px 22px 0 0;background:{SURF};box-shadow:0 -2px 24px rgba(16,24,40,.16)">'
    f'<div style="width:38px;height:4px;margin:8px auto 2px;border-radius:2px;background:{LINE}"></div>'
    f'<div style="display:flex;flex-direction:column;gap:10px;padding:8px 16px 0">'
    f'<div style="display:flex;align-items:center;gap:8px;height:42px;padding:0 12px;border-radius:999px;background:{SURF2};box-shadow:0 0 0 2px rgba(46,192,106,.45);font-size:15px;color:{INK}">{ic("search",18,"color:#7b838e;")}价格<span style="display:inline-block;width:1.5px;height:17px;background:{INK};vertical-align:-3px;margin-left:1px"></span><span style="margin-left:auto;font-size:12px;color:{TIME}">3 条</span></div>'
    f'<div style="font-size:11.5px;font-weight:700;color:{MUTED};letter-spacing:.06em">最近用过</div>'
    f'<div style="display:flex;gap:6px;overflow:hidden">{recent_chip("WNSM 价格")}{recent_chip("KL 地址 + 停车")}{recent_chip("PTPK 三样文件")}{recent_chip("周六试听")}</div>'
    f'<div style="font-size:11.5px;font-weight:700;color:{MUTED};letter-spacing:.06em;margin-top:2px">搜到 · 按用过次数</div>'
    + qrow('WNSM KL CN- PRICE', '用过 132 次 · 1 步 · 1 图 · 资料夹 WNSM KL CN', True, True)
    + qrow('WNSM KL CN- SCHEDULE 2026', '用过 87 次 · 2 步 · 2 图')
    + qrow('FMC WEEKEND KL CN- PRICE', '用过 64 次 · 1 步 · 1 图')
    + f'<div style="display:flex;gap:6px;overflow:hidden;padding-top:4px">{recent_chip("资料夹：WNSM KL CN")}{recent_chip("FMC WEEKEND KL CN")}{recent_chip("WINE KL CN")}</div>'
    + '</div>'
    # 预览浮层
    + f'<div style="margin:auto 12px 20px;padding:12px 12px 12px;border-radius:14px;background:{SURF};border:1px solid {LINE};box-shadow:0 8px 28px rgba(16,24,40,.18)">'
    f'<div style="display:flex;align-items:center;gap:6px;margin-bottom:8px"><span style="font-size:13.5px;font-weight:700">📌 WNSM KL CN- PRICE</span><span style="font-size:12px;color:{MUTED}">· 发出去是这样</span></div>'
    f'<div style="display:flex;gap:8px;align-items:flex-start"><div style="width:64px;height:64px;flex:none;border-radius:8px;background:#efe7dd;border:1px solid {LINE};display:flex;align-items:center;justify-content:center;color:#c79a63">{ic("image",22)}</div>'
    f'<p style="margin:0;flex:1;min-width:0;padding:8px 10px;border-radius:9px;background:{ACCENT};font-size:13px;line-height:1.4;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden">调酒半工读 WNSM 学费 RM ___ ，可分期 / PTPK。9 月班 16/9 开课，一周 1 天。图是课程表 👆</p></div>'
    f'<div style="display:grid;grid-template-columns:repeat(2, minmax(0, 1fr));gap:8px;margin-top:10px">'
    f'<div style="min-height:42px;display:flex;align-items:center;justify-content:center;border-radius:10px;background:{BRAND};color:#ffffff;font-size:14px;font-weight:700">发送 · 1 图 + 文字</div>'
    f'<div style="min-height:42px;display:flex;align-items:center;justify-content:center;border-radius:10px;border:1px solid {LINE};background:{SURF};font-size:14px;font-weight:600;color:{INK2}">只填文字，我再改</div></div></div></div>')
quick_inner = (header2('Sharon', '🍷', 'Emily 线', st('你在回','green') + st('Bot 已停','green') + st('对客户显示 Emily','gray'))
    + ctxline(['WNSM 调酒半工读', '中文', '热'])
    + stream2([bubble_in(SHARON_Q, '11:04')]) + composer2('', '以 Emily 的身份回复…')
    + scrim() + quick_drawer)
(OUT/'Quick.dc.html').write_text(phone(quick_inner))

# ══════════ 6. Queue —— 队列（次要入口）：谁在回看得见 ══════════
def qrow2(initial, emoji, name, wait, level, question, tags_html, claimed_by=None, mine=False):
    if claimed_by:
        right = f'<div style="align-self:center;padding:5px 9px;border-radius:7px;background:{SURF2};color:{MUTED};font-size:11.5px;font-weight:700;white-space:nowrap">{claimed_by} 在回</div>'
        op = 'opacity:.55;'; bg = SURF
    else:
        right = f'<div style="align-self:center;width:44px;height:44px;display:flex;align-items:center;justify-content:center;border-radius:10px;background:{SURF2};color:{INK}">{ic("bolt",19)}</div>'
        op = ''; bg = BRAND_SOFT
    if mine:
        right = f'<div style="align-self:center;padding:5px 9px;border-radius:7px;background:{BRAND};color:#ffffff;font-size:11.5px;font-weight:700;white-space:nowrap">你在回</div>'; op=''; bg = SURF
    return (f'<div style="display:grid;grid-template-columns:42px minmax(0,1fr) auto;gap:11px;align-items:start;padding:12px 12px 12px 16px;border-bottom:1px solid {LINE_SOFT};background:{bg};{op}">'
            f'{avatar(initial, emoji)}'
            f'<div style="min-width:0;display:flex;flex-direction:column;gap:3px">'
            f'<div style="display:flex;align-items:baseline;gap:8px"><span style="flex:1;min-width:0;font-size:15px;font-weight:600;letter-spacing:-.01em;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{name}</span>{wait_pill(wait, level)}</div>'
            f'<p style="margin:0;font-size:13.5px;line-height:1.38;color:{MUTED};display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden">{question}</p>'
            f'<div style="display:flex;flex-wrap:wrap;gap:5px;margin-top:3px">{tags_html}</div></div>{right}</div>')
queue_inner = (f'<div style="display:flex;align-items:center;gap:8px;padding:16px 8px 6px 16px"><h1 style="margin:0;font-size:21px;font-weight:700;letter-spacing:-.015em">待回</h1><span style="font-size:12.5px;color:{MUTED};margin-top:6px">主动清的时候才来这里</span><span style="flex:1"></span>{iconbtn("search")}{iconbtn("gear")}</div>'
    f'<div style="display:flex;gap:8px;padding:2px 16px 10px;overflow:hidden">{chip("全部线", True, 8)}{chip("🍷 Emily", False, 1)}{chip("☕ Cindy", False, 1)}{chip("☕ Coco", False, 1)}{chip("🏢 主号", False, 5)}</div>'
    + section('🆘 等真人', 3, '最久没回的在最上')
    + qrow2('S','🍷','Sharon','等 14 分','hot', SHARON_Q, tag('WNSM 调酒半工读','blue')+stage_tag('hot'), mine=True)
    + qrow2('W','☕','Wei Jie','等 7 分','warm','BMART diploma 是不是 PTPK 可以全额？我 SPM 只有 3 credit 够吗', tag('BMART Diploma','blue')+stage_tag('considering'), claimed_by='佳佳')
    + qrow2('A','☕','Aina','等 3 分','cool','Kelas Barista 1 hari tu hujung minggu ada tak? Berapa harga ya?', tag('1-Day Junior Barista (BM/EN)','blue')+stage_tag('curious'))
    + section('🏢 主号未回', 5, '真人线，没有 bot')
    + qrow2('J','🏢','Jason Lim','未回 2 小时','hot','老师，明天的 FCC 课几点到？停车在哪', tag('FCC 咖啡周末班','blue')+tag('在读学员','green'))
    + qrow2('M','🏢','Mei Ling','未回 40 分','warm','请问 sourdough 课还有位吗', tag('Sourdough 2-Day','blue'))
    + f'<div style="display:flex;align-items:center;gap:8px;padding:12px 16px;border-top:1px solid {LINE_SOFT};font-size:14px;font-weight:600;color:{INK}">{ic("phone",18,"color:#3c444e;")}<span style="flex:1">IG/FB 给了号码，等你打</span><span class="num" style="color:{BRAND}">2</span>{ic("chevron",16,"color:#9aa1ab;","2")}</div>'
    + dock(primary('开始清队列', '· 7 条（跳过别人在回的）')))
(OUT/'Queue.dc.html').write_text(phone(queue_inner))

# ══════════ 7. Failed —— 送不出去，大声且带下一步（Nurul · IG · Coco 线）══════════
fail_inner = (header2('Nurul', '☕', 'Coco 线 · IG', st('你在回','green') + st('Bot 已停','green') + st('对客户显示 Coco','gray'))
    + ctxline(['BWC Bakery Weekend', 'BM · 自动翻译', '考虑中'], '⚠ IG 24 小时窗口已关')
    + stream2([daysep('前天'),
               bubble_in_tr('my number 012-345 6789, boleh call petang. Nak tanya pasal kelas roti weekend tu', '前天 15:10', '我的号码 012-345 6789，下午可以打。想问周末面包课的事'),
               bubble_out('Hai Nurul, boleh! Kelas Bakery Weekend seterusnya 27 Sept. Saya WhatsApp awak sekejap lagi ya 🙂', '16:42', 'Boon · 人手（客户看到的是 Coco）', 'failed'),
               f'<div style="margin:0 2px;padding:12px;border-radius:10px;background:{SURF};border:1.5px solid #c0392b">'
               f'<div style="display:flex;align-items:center;gap:6px;font-size:13.5px;font-weight:700;color:#c0392b">❌ 没发出去：IG 私信 24 小时窗口已关</div>'
               f'<div style="margin-top:3px;font-size:12.5px;line-height:1.4;color:{INK2}">客户上次发言 前天 15:10，超过 24 小时 Instagram 不让主动发。她留了 WhatsApp 号码，下一步：</div>'
               f'<div style="display:flex;flex-direction:column;gap:6px;margin-top:10px">'
               f'<div style="min-height:42px;display:flex;align-items:center;justify-content:center;gap:7px;border-radius:10px;background:{BRAND};color:#ffffff;font-size:14px;font-weight:700">{ic("wa",17)}WhatsApp 她 · 012-345 6789</div>'
               f'<div style="display:grid;grid-template-columns:repeat(2, minmax(0, 1fr));gap:6px">'
               f'<div style="min-height:40px;display:flex;align-items:center;justify-content:center;gap:6px;border-radius:10px;border:1px solid {LINE};background:{SURF};font-size:13.5px;font-weight:600;color:{INK2}">{ic("phone",16)}打电话</div>'
               f'<div style="min-height:40px;display:flex;align-items:center;justify-content:center;border-radius:10px;border:1px solid {LINE};background:{SURF};font-size:13.5px;font-weight:600;color:{INK2}">等她再发来</div></div></div></div>'])
    + f'<div style="display:flex;align-items:center;gap:8px;padding:9px 12px;border-top:1px solid {LINE};background:{SURF};font-size:12.5px;color:{MUTED}">{ic("info",15,"color:#7b838e;","2")}这条会留在「IG/FB 给了号码」名单里，打了就点「已联系」。</div>'
    + composer2('', 'IG 这边现在发不出去', disabled=False))
(OUT/'Failed.dc.html').write_text(phone(fail_inner, CANVAS))

# ══════════ canvas.json：两页 ══════════
W,H,G = 390,844,80
def x(i): return i*(W+G)
v2_boards = [
    {"file":"Notify.dc.html","x":x(0),"y":0,"w":W,"h":260,"title":"0 · 通知 → 直达","page":"v2"},
    {"file":"Main.dc.html",  "x":x(1),"y":0,"w":W,"h":H,"title":"1 · 会话（从通知进来）","page":"v2"},
    {"file":"Reply.dc.html", "x":x(2),"y":0,"w":W,"h":H,"title":"2 · 翻译内建 + 草稿写答案","page":"v2"},
    {"file":"Gate.dc.html",  "x":x(3),"y":0,"w":W,"h":H,"title":"3 · 从队列进来 · 先停 bot","page":"v2"},
    {"file":"Sent.dc.html",  "x":x(0),"y":1020,"w":W,"h":H,"title":"4 · 发完一行提示","page":"v2"},
    {"file":"Quick.dc.html", "x":x(1),"y":1020,"w":W,"h":H,"title":"5 · 话术先搜索 · 插入前预览","page":"v2"},
    {"file":"Queue.dc.html", "x":x(2),"y":1020,"w":W,"h":H,"title":"6 · 队列 · 谁在回","page":"v2"},
    {"file":"Failed.dc.html","x":x(3),"y":1020,"w":W,"h":H,"title":"7 · 送不出去 → 下一步","page":"v2"},
]
v1_boards = []
for b in v1_canvas['artboards']:
    stem = b['file'].replace('.dc.html','')
    b2 = dict(b); b2['file'] = V1[stem] + '.dc.html'; b2['page'] = 'v1'; b2['title'] = 'v1 · ' + b.get('title', stem)
    v1_boards.append(b2)
v1_notes = []
for a in v1_canvas.get('annotations', []):
    a2 = dict(a); a2['id'] = 'v1-' + a['id']; a2['page'] = 'v1'; v1_notes.append(a2)
v2_notes = [
    {"id":"v2-map","x":x(0),"y":-420,"w":980,"page":"v2","text":"v2 · 十条全部落进画板：\n① 从通知直达 → 画板 0 + 1：点通知 = 认领 + 停 bot + 键盘弹出，四步变一步。\n② 客户问的那句钉在键盘上方 → 每屏的红框「🆘 客户在问」；上下文收成一行：课程 · 语言 · 阶段 · 地雷。\n③ 语言自动跟客户、翻译内建 → 画板 2：BM 消息下面一行灰色中文；我用中文写，发出时翻成 BM，可切回发中文。\n④ 草稿标签写答案 → 画板 1、2：粗体那行就是答案，两条 + 换一批。\n⑤ 主操作放底部 → 画板 3：bot 还在回时输入框灰着，上面一行「停 bot 并回复」点一下就停并聚焦。若改成「手动回复一律自动停 bot」这条灰条整个消失。\n⑥ 发完不逼决定 → 画板 4：一行「已发 · 12 小时后 Bot 接回 · 现在交还」，清队列模式才出「下一条」。\n⑦ 话术先搜索 → 画板 5：搜索框置顶、最近用过、按用过次数；带图模板插入前预览。\n⑧ 以谁的名义说话 → 每屏标题下「对客户显示 Emily」，输入框占位「以 Emily 的身份回复」，自己的名字只在内部气泡标签上。规则按默认（延续线的人设）画，要改一句话。\n⑨ 队列看得见谁在回 → 画板 6：「佳佳 在回」灰掉、「你在回」绿色，清队列自动跳过别人的。\n⑩ 送不出去带下一步 → 画板 7：IG 24 小时窗口关了直接给 WhatsApp / 打电话 / 等她再发。"},
    {"id":"v2-backend","x":x(0)+1060,"y":-420,"w":600,"page":"v2","text":"你确认之前不动代码。届时后端要加的：\n· 带登录态的认领 POST（①）\n· 翻译（③）：进来的 BM/EN → 中文，出去的中文 → 客户语言\n· AI 草稿（④）：只准用 Sheet 目录里的事实\n· 主号「谁还没被回」端点（⑨ 的第二段）\n· 若采纳「手动回复一律自动停 bot」→ 改一条规则（⑤）\n其它都是现有接口。人名、消息、价格皆为示例，RM ___ 处由 Sheet 目录填。"},
    {"id":"v2-n1","x":x(1),"y":900,"w":W,"page":"v2","text":"这一屏就是 80% 的使用场景：通知点开落在这里。已认领、Bot 已停，键盘已弹出。往上滑才是聊天记录，往下什么都不用找。"},
    {"id":"v2-n2","x":x(2),"y":900,"w":W,"page":"v2","text":"中文同事回马来客户的全部动作：看灰色译文 → 点草稿或用中文打 → 发出时自动翻成 BM。地雷「BM 渠道不放酒精」照 dashboard 现有规则。"},
    {"id":"v2-n3","x":x(3),"y":900,"w":W,"page":"v2","text":"只有从队列主动点进来才会看到这一屏（Aina 是队列里唯一没人认领的）。「停 bot 并回复」一下，就变成画板 2 的状态。"},
]
canvas = {
  "pages": [{"id":"v2","name":"v2 · 照十条改"}, {"id":"v1","name":"v1 · 存档"}],
  "artboards": v2_boards + v1_boards,
  "annotations": v2_notes + v1_notes,
  "launch": {"view":"canvas","page":"v2"},
}
(OUT/'canvas.json').write_text(json.dumps(canvas, ensure_ascii=False, indent=2))
for f in sorted(OUT.iterdir()): print(f.name, f.stat().st_size)
