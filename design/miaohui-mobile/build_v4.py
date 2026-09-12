# v4 —— 只画员工看得到的。只借 v1/v2 的小组件（不跑它们的文件写入），文案重写：界面上不出现接口、规则、开关。
import json, pathlib
SCR = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(__file__).resolve().parent
ns = {}
s1 = (SCR / 'build.py').read_text()
helpers, rest = s1.split('# ══════════════════════════ 1. Main —— 待回队列', 1)
exec(helpers, ns)
shared = rest.split('# ══════════════════════════ 2. Chat —— 会话 · 接管', 1)[0].split('# ══════════════════════════ 会话相关共用 ══════════════════════════', 1)[1]
exec(shared, ns)
s2 = (SCR / 'build_v2.py').read_text()
exec(s2.split('HOT_BG, HOT_FG', 1)[1].split('# ── 1) v1 存档', 1)[0].split('\n', 1)[1], ns)   # sos_marker2, scrim
exec(s2.split('# ── v2 小组件 ──', 1)[1].split('# ══════════ 0. Notify', 1)[0], ns)              # header2, st, ctxline, task_card, draft_card, composer2, bubble_in_tr, stream2 ...
for k in ['INK','INK2','MUTED','TIME','LINE','LINE_SOFT','SURF','SURF2','CANVAS','BRAND','BRAND_SOFT','ACCENT','WARM','LINK','TAG','WAIT','STAGE','HEAD','TAIL',
          'ic','phone','iconbtn','tag','stage_tag','wait_pill','avatar','chip','section','primary','dock','bubble_in','bubble_out','daysep',
          'st','bubble_in_tr','stream2','scrim']:
    globals()[k] = ns[k]
SHARON_Q = '刚毕业。如果中途找到全职工作可以转周末班吗？学费怎么算？'
AINA_Q = 'Kelas Barista 1 hari tu hujung minggu ada tak? Berapa harga ya?'
EMILY_HELLO = '哈喽 Sharon，我是 Emily 🍷 调酒半工读是 9 个月 36 堂，一周上 1 天课，其余时间在合作酒吧带薪实习。你现在是在工作，还是刚毕业？'
BOON_REPLY = '可以的 Sharon，半工读转周末班随时可以，学费按剩余堂数折算，不会重复收。刚毕业的话建议先来看一堂实操（免费），这周六 2 点有一场，帮你留位？'

# ── v4 小组件：文案只留员工用得上的 ──
def header4(name, emoji, line, status, kind='green'):
    return (f'<div style="display:flex;align-items:center;gap:6px;padding:8px 8px 8px 2px;border-bottom:1px solid {LINE};background:{SURF}">'
            f'<div style="width:40px;height:44px;display:flex;align-items:center;justify-content:center;color:{INK}">{ic("chevron",22,"transform:scaleX(-1);")}</div>'
            f'{avatar(name[0], emoji, 36)}'
            f'<div style="flex:1;min-width:0"><div style="font-size:16px;font-weight:700;letter-spacing:-.015em;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{name}</div>'
            f'<div style="font-size:12px;color:{MUTED};white-space:nowrap">{emoji} {line}</div></div>'
            f'{st(status, kind)}<div style="width:40px;height:44px;display:flex;align-items:center;justify-content:center;color:{INK2}">{ic("more",20)}</div></div>')
def ctx4(parts, warn=None):
    w = f'<span style="color:#c0392b;font-weight:700">{warn}</span>' if warn else ''
    return (f'<div style="display:flex;align-items:center;gap:6px;padding:7px 16px;border-bottom:1px solid {LINE_SOFT};background:{SURF};font-size:12.5px;color:{INK2};white-space:nowrap;overflow:hidden">'
            + '<span style="color:#9aa1ab">·</span>'.join(f'<span style="font-weight:600">{p}</span>' for p in parts) + (f'<span style="color:#9aa1ab">·</span>{w}' if w else '') + '</div>')
def task4(question, wait_text, level='hot', title='客户在问'):
    bg, fg = WAIT[level]
    return (f'<div style="margin:0 12px;padding:10px 12px;border-radius:10px;background:{SURF};border:1.5px solid {fg};box-shadow:0 1px 1px rgba(16,24,40,.09)">'
            f'<div style="display:flex;align-items:center;gap:6px;margin-bottom:4px"><span style="font-size:11px;font-weight:700;color:{fg};letter-spacing:.04em">{title}</span><span class="num" style="margin-left:auto;padding:1px 7px;border-radius:7px;background:{bg};color:{fg};font-size:11px;font-weight:700">{wait_text}</span></div>'
            f'<div style="font-size:14.5px;font-weight:600;line-height:1.4;color:{INK}">{question}</div></div>')
def draft4(answer, body, gloss=''):
    g = f'<div style="margin-top:5px;font-size:11.5px;color:{TIME};white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{gloss}</div>' if gloss else ''
    return (f'<div style="flex:none;width:286px;padding:10px 12px;border:1px solid {LINE};border-radius:10px;background:{SURF}">'
            f'<div style="font-size:14px;font-weight:700;color:{INK};margin-bottom:4px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{answer}</div>'
            f'<p style="margin:0;font-size:13px;line-height:1.42;color:{INK2};display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden">{body}</p>{g}</div>')
def drafts4(cards, label='草稿', more='换一批'):
    return (f'<div style="display:flex;align-items:center;gap:6px;padding:8px 12px 0;font-size:11.5px;font-weight:700;color:{MUTED};letter-spacing:.04em">{ic("asterisk",13,"color:#7b838e;")}{label}'
            f'<span style="margin-left:auto;padding:4px 10px;border-radius:999px;background:{SURF2};color:{INK};font-size:12px;font-weight:700;letter-spacing:0">{more}</span></div>'
            f'<div style="display:flex;gap:8px;padding:8px 12px 0;overflow:hidden">{"".join(cards)}</div>')
def composer4(text='', placeholder='以 Emily 的身份回复…', focused=False, gate=None):
    field_col = INK if text else (TIME if gate else MUTED)
    cursor = f'<span style="display:inline-block;width:1.5px;height:17px;background:{INK};vertical-align:-3px;margin-left:1px"></span>' if focused else ''
    ring = 'box-shadow:0 0 0 2px rgba(46,192,106,.45);' if focused else ''
    field = f'<div style="flex:1;min-width:0;min-height:40px;padding:9px 14px;border-radius:22px;background:{SURF2};font-size:15px;line-height:1.4;color:{field_col};{ring}">{text or placeholder}{cursor}</div>'
    send_bg = BRAND if text else SURF2; send_fg = '#ffffff' if text else MUTED
    bar = (f'<div style="display:flex;align-items:center;gap:8px;margin:8px 8px 8px;padding:10px 12px;border-radius:10px;background:#fdf3c9;color:#7a5f18;font-size:13.5px;font-weight:700">'
           f'<span style="flex:1">{gate}</span><span style="display:flex;align-items:center;gap:4px;white-space:nowrap">🔴 停 bot 并回复 {ic("chevron",14,"","2.2")}</span></div>') if gate else ''
    return (f'<div style="border-top:1px solid {LINE};background:{SURF}">{bar}<div style="display:flex;align-items:flex-end;gap:4px;padding:{"0" if gate else "8px"} 8px 20px;{"opacity:.5;" if gate else ""}">'
            f'<div style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;color:{INK2}">{ic("asterisk",20)}</div>{field}'
            f'<div style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;color:{INK2}">{ic("mic",20)}</div>'
            f'<div style="width:40px;height:40px;flex:none;display:flex;align-items:center;justify-content:center;border-radius:50%;background:{send_bg};color:{send_fg}">{ic("send",20)}</div></div></div>')
def toast4(text_html, btn):
    return (f'<div style="display:flex;align-items:center;gap:8px;padding:9px 12px;border-top:1px solid {LINE};background:{SURF};font-size:13px;color:{INK2}">'
            f'{ic("check2",16,"color:#2ec06a;","2.2")}<span style="flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{text_html}</span>'
            f'<span style="flex:none;padding:6px 10px;border-radius:999px;background:{SURF2};font-size:12.5px;font-weight:700;color:{INK};white-space:nowrap">{btn}</span></div>')
def fail_card(title, line, primary_html, left, right):
    return (f'<div style="margin:0 2px;padding:12px;border-radius:10px;background:{SURF};border:1.5px solid #c0392b">'
            f'<div style="font-size:13.5px;font-weight:700;color:#c0392b">❌ {title}</div>'
            f'<div style="margin-top:3px;font-size:12.5px;line-height:1.4;color:{INK2}">{line}</div>'
            f'<div style="display:flex;flex-direction:column;gap:6px;margin-top:10px">{primary_html}'
            f'<div style="display:grid;grid-template-columns:repeat(2, minmax(0, 1fr));gap:6px">'
            f'<div style="min-height:40px;display:flex;align-items:center;justify-content:center;gap:6px;border-radius:10px;border:1px solid {LINE};background:{SURF};font-size:13.5px;font-weight:600;color:{INK2}">{left}</div>'
            f'<div style="min-height:40px;display:flex;align-items:center;justify-content:center;border-radius:10px;border:1px solid {LINE};background:{SURF};font-size:13.5px;font-weight:600;color:{INK2}">{right}</div></div></div></div>')
def big_btn(label, sub='', bg=None, fg='#ffffff'):
    bg = bg or BRAND
    s_ = f'<span style="font-size:11.5px;font-weight:500;opacity:.85;margin-top:2px">{sub}</span>' if sub else ''
    return f'<div style="min-height:{48 if sub else 44}px;display:flex;flex-direction:column;align-items:center;justify-content:center;border-radius:10px;background:{bg};color:{fg};font-size:14.5px;font-weight:700;line-height:1.2">{label}{s_}</div>'

SHARON_STREAM = [daysep('今天'), bubble_in('你好 我看到调酒半工读的广告', '11:02'), bubble_out(EMILY_HELLO, '11:02', 'Emily · Bot'), bubble_in(SHARON_Q, '11:04')]

# ══ 0 通知 ══
notify = (f'<div style="width:390px;height:200px;background:{CANVAS};display:flex;flex-direction:column;gap:10px;padding:16px;box-sizing:border-box;font-size:15px;line-height:1.45">'
    f'<div style="font-size:11.5px;font-weight:700;color:{MUTED};letter-spacing:.06em">通知</div>'
    f'<div style="display:flex;gap:11px;padding:12px 14px;border-radius:14px;background:{SURF};box-shadow:0 1px 2px rgba(16,24,40,.05), 0 8px 24px rgba(16,24,40,.10)">'
    f'<div style="width:38px;height:38px;flex:none;border-radius:10px;background:{BRAND};color:#ffffff;display:flex;align-items:center;justify-content:center">{ic("bolt",20,"color:#ffffff;","2")}</div>'
    f'<div style="flex:1;min-width:0"><div style="display:flex;align-items:baseline;gap:6px"><span style="font-size:14.5px;font-weight:700">🆘 Sharon 等了 <span class="num" style="color:#c0392b">14 分</span></span><span class="num" style="margin-left:auto;font-size:11.5px;color:{TIME}">11:18</span></div>'
    f'<div style="font-size:13.5px;line-height:1.4;color:{INK2};margin-top:2px">🍷 Emily 线 · {SHARON_Q}</div>'
    f'<div style="font-size:12px;color:{MUTED};margin-top:4px">值班：你、佳佳 · 先点先得</div></div></div></div>')
(OUT/'Notify.dc.html').write_text(HEAD + notify + TAIL)

# ══ 1 会话 ══
main_inner = (header4('Sharon', '🍷', 'Emily 线', 'Bot 已停')
    + ctx4(['WNSM 调酒半工读', '中文', '热'])
    + stream2(SHARON_STREAM)
    + f'<div style="background:{WARM};padding:0 0 10px">{task4(SHARON_Q, "等了 14 分")}</div>'
    + drafts4([draft4('可以转，按剩余堂数折算', BOON_REPLY), draft4('先问：边找工作还是专心学', 'Sharon 你好，想先了解一下：你是想边找工作边学，还是先专心学完 9 个月？两种情况推荐的班不一样。')])
    + composer4('', '以 Emily 的身份回复…', focused=True))
(OUT/'Main.dc.html').write_text(phone(main_inner))

# ══ 2 翻译（Aina · Coco · BM）══
AINA_STREAM = [daysep('今天'),
    bubble_in_tr('Hai, saya nampak iklan kelas barista. Untuk yang tak ada pengalaman boleh ke?', '11:12', '你好，我看到咖啡师课程的广告。没有经验的可以吗？'),
    bubble_out('Hai Aina ☕ Boleh! Kelas 1 hari ni memang untuk yang baru nak mula.', '11:12', 'Coco · Bot'),
    bubble_in_tr(AINA_Q, '11:15', '一日咖啡师课周末有场吗？多少钱？')]
reply_inner = (header4('Aina', '☕', 'Coco 线', 'Bot 已停')
    + ctx4(['1-Day Junior Barista', 'BM', '好奇'], '⚠ 不提酒精')
    + stream2(AINA_STREAM)
    + f'<div style="background:{WARM};padding:0 0 10px">{task4("周末有场吗？多少钱？", "等了 3 分", "cool")}</div>'
    + drafts4([draft4('有周末场 · 下一场 20/9 · 报价', 'Ada! Sesi hujung minggu seterusnya 20 Sept (Sabtu), 10 pagi–2 petang. Harga RM ___ termasuk bahan &amp; sijil kehadiran. Nak saya simpan tempat?', '中文：有！下一场周末 9 月 20 日周六 10–2 点，RM ___ 含材料和出席证明，要留位吗？'),
               draft4('先问：几位一起来', 'Sebelum saya bagi harga, awak datang seorang atau berdua? Harga berdua lain sikit.', '中文：报价前先问，一个人还是两个人来？双人价不同。')])
    + f'<div style="display:flex;align-items:center;gap:8px;margin:10px 8px 0;padding:9px 12px;border-radius:10px;background:{BRAND_SOFT};font-size:12.5px;line-height:1.4;color:#1e7a45">'
    f'<span style="font-weight:700;white-space:nowrap">发出时翻成 BM ✓</span><span style="flex:1;min-width:0;color:#3c7a55;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">Ada! Sesi hujung minggu seterusnya 20 Sept, 10 pagi…</span><span style="font-weight:700;white-space:nowrap;color:{MUTED}">发中文</span></div>'
    + composer4('有的！下一场周末班 9 月 20 日周六早上 10 点，要帮你留位吗？', '', focused=True))
(OUT/'Reply.dc.html').write_text(phone(reply_inner))

# ══ 3 先停 bot（从队列点进 Aina）══
gate_inner = (header4('Aina', '☕', 'Coco 线', 'Bot 在回', 'yellow')
    + ctx4(['1-Day Junior Barista', 'BM', '好奇'], '⚠ 不提酒精')
    + stream2(AINA_STREAM)
    + f'<div style="background:{WARM};padding:0 0 10px">{task4("周末有场吗？多少钱？", "等了 3 分", "cool")}</div>'
    + composer4('', '以 Coco 的身份回复…', gate='Bot 还在回，先停它'))
(OUT/'Gate.dc.html').write_text(phone(gate_inner))

# ══ 4 发完 ══
sent_inner = (header4('Sharon', '🍷', 'Emily 线', 'Bot 已停')
    + ctx4(['WNSM 调酒半工读', '中文', '热'])
    + stream2(SHARON_STREAM + [bubble_out(BOON_REPLY, '11:19', 'Boon', 'read')])
    + toast4(f'<span style="font-weight:600">已发 ✓✓</span><span style="color:{MUTED}"> · 12 小时后 Bot 接回</span>', '🟢 交还')
    + composer4('', '以 Emily 的身份回复…')
    + f'<div style="display:flex;align-items:center;gap:10px;padding:10px 16px 20px;margin-top:-12px;background:{INK};color:#ffffff">'
    f'<div style="flex:1;min-width:0;font-size:14px;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap"><span style="color:rgba(255,255,255,.7)">下一条</span> Aina · ☕ Coco 线 · <span class="num" style="color:#6fdc9b">等 4 分</span></div>'
    f'<div style="flex:none;height:40px;padding:0 14px;display:flex;align-items:center;gap:6px;border-radius:10px;background:{BRAND};color:#ffffff;font-size:14px;font-weight:700">下一条 {ic("chevron",16,"","2")}</div></div>')
(OUT/'Sent.dc.html').write_text(phone(sent_inner))

# ══ 5 话术 ══
def rchip(text, on=False):
    st_ = f'background:{INK};color:#ffffff' if on else f'background:{SURF2};color:{INK}'
    return f'<div style="flex:none;height:32px;padding:0 12px;display:flex;align-items:center;border-radius:999px;font-size:12.5px;font-weight:600;white-space:nowrap;{st_}">{text}</div>'
def qrow(name, meta, on=False):
    return (f'<div style="display:flex;align-items:center;gap:10px;padding:10px 8px;margin:0 -8px;border-radius:8px;background:{BRAND_SOFT if on else "transparent"}">'
            f'<div style="flex:1;min-width:0"><div style="font-size:14px;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{name}</div><div style="font-size:12px;color:{MUTED}">{meta}</div></div>{ic("chevron",16,"color:#9aa1ab;","2")}</div>')
quick_drawer = (f'<div style="position:absolute;left:0;right:0;bottom:0;height:640px;display:flex;flex-direction:column;border-radius:22px 22px 0 0;background:{SURF};box-shadow:0 -2px 24px rgba(16,24,40,.16)">'
    f'<div style="width:38px;height:4px;margin:8px auto 2px;border-radius:2px;background:{LINE}"></div>'
    f'<div style="display:flex;flex-direction:column;gap:10px;padding:8px 16px 0">'
    f'<div style="display:flex;align-items:center;gap:8px;height:42px;padding:0 12px;border-radius:999px;background:{SURF2};box-shadow:0 0 0 2px rgba(46,192,106,.45);font-size:15px;color:{INK}">{ic("search",18,"color:#7b838e;")}价格<span style="display:inline-block;width:1.5px;height:17px;background:{INK};vertical-align:-3px;margin-left:1px"></span></div>'
    f'<div style="display:flex;gap:6px;overflow:hidden">{rchip("最近：WNSM 价格")}{rchip("KL 地址")}{rchip("PTPK 文件")}{rchip("周六试听")}</div>'
    + qrow('WNSM KL CN- PRICE', '📌 置顶 · 1 图', True)
    + qrow('WNSM KL CN- SCHEDULE 2026', '2 图')
    + qrow('FMC WEEKEND KL CN- PRICE', '1 图')
    + f'<div style="display:flex;gap:6px;overflow:hidden;padding-top:2px">{rchip("WNSM KL CN")}{rchip("FMC WEEKEND KL CN")}{rchip("WINE KL CN")}</div>'
    + '</div>'
    + f'<div style="margin:auto 12px 20px;padding:12px;border-radius:14px;background:{SURF};border:1px solid {LINE};box-shadow:0 8px 28px rgba(16,24,40,.18)">'
    f'<div style="font-size:13.5px;font-weight:700;margin-bottom:8px">📌 WNSM KL CN- PRICE</div>'
    f'<div style="display:flex;gap:8px;align-items:flex-start"><div style="width:64px;height:64px;flex:none;border-radius:8px;background:#efe7dd;border:1px solid {LINE};display:flex;align-items:center;justify-content:center;color:#c79a63">{ic("image",22)}</div>'
    f'<p style="margin:0;flex:1;min-width:0;padding:8px 10px;border-radius:9px;background:{ACCENT};font-size:13px;line-height:1.4;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden">调酒半工读 WNSM 学费 RM ___ ，可分期 / PTPK。9 月班 16/9 开课，一周 1 天。图是课程表 👆</p></div>'
    f'<div style="display:grid;grid-template-columns:repeat(2, minmax(0, 1fr));gap:8px;margin-top:10px">{big_btn("发送")}{big_btn("只填文字，我再改", "", SURF, INK2).replace("background:#ffffff", "background:#ffffff;border:1px solid #e9eaec")}</div></div></div>')
quick_inner = (header4('Sharon', '🍷', 'Emily 线', 'Bot 已停') + ctx4(['WNSM 调酒半工读', '中文', '热'])
    + stream2([bubble_in(SHARON_Q, '11:04')]) + composer4('', '以 Emily 的身份回复…') + scrim() + quick_drawer)
(OUT/'Quick.dc.html').write_text(phone(quick_inner))

# ══ 6 待回 ══
def row6(initial, emoji, name, pill_text, level, question, tags_html, state='open', who=''):
    if state == 'mine':
        right = f'<div style="align-self:center;padding:5px 9px;border-radius:7px;background:{BRAND};color:#ffffff;font-size:11.5px;font-weight:700;white-space:nowrap">你在回</div>'; op=''; bg=SURF
    elif state == 'other':
        right = f'<div style="align-self:center;padding:5px 9px;border-radius:7px;background:{SURF2};color:{MUTED};font-size:11.5px;font-weight:700;white-space:nowrap">{who} 在回</div>'; op='opacity:.55;'; bg=SURF
    else:
        right = f'<div style="align-self:center;width:44px;height:44px;display:flex;align-items:center;justify-content:center;border-radius:10px;background:{SURF2};color:{INK}">{ic("bolt",19)}</div>'; op=''; bg=BRAND_SOFT
    return (f'<div style="display:grid;grid-template-columns:42px minmax(0,1fr) auto;gap:11px;align-items:start;padding:12px 12px 12px 16px;border-bottom:1px solid {LINE_SOFT};background:{bg};{op}">'
            f'{avatar(initial, emoji)}<div style="min-width:0;display:flex;flex-direction:column;gap:3px">'
            f'<div style="display:flex;align-items:baseline;gap:8px"><span style="flex:1;min-width:0;font-size:15px;font-weight:600;letter-spacing:-.01em;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{name}</span>{wait_pill(pill_text, level)}</div>'
            f'<p style="margin:0;font-size:13.5px;line-height:1.38;color:{MUTED};display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden">{question}</p>'
            f'<div style="display:flex;flex-wrap:wrap;gap:5px;margin-top:3px">{tags_html}</div></div>{right}</div>')
def link_row(icon, label, count):
    return f'<div style="display:flex;align-items:center;gap:8px;padding:13px 16px;border-top:1px solid {LINE_SOFT};font-size:14px;font-weight:600;color:{INK}">{ic(icon,18,"color:#3c444e;")}<span style="flex:1">{label}</span><span class="num" style="color:{BRAND}">{count}</span>{ic("chevron",16,"color:#9aa1ab;","2")}</div>'
queue_inner = (f'<div style="display:flex;align-items:center;gap:8px;padding:16px 8px 4px 16px"><h1 style="margin:0;font-size:21px;font-weight:700;letter-spacing:-.015em">待回</h1><span style="flex:1"></span>'
    f'<div style="display:flex;align-items:center;gap:6px;height:32px;padding:0 10px 0 8px;border-radius:999px;background:{BRAND_SOFT};color:#1e7a45;font-size:12.5px;font-weight:700"><span style="width:8px;height:8px;border-radius:50%;background:{BRAND}"></span>值班中</div>{iconbtn("gear")}</div>'
    f'<div style="padding:0 16px 8px;font-size:12.5px;color:{MUTED}">值班：<b style="color:{INK2}">你、佳佳</b></div>'
    f'<div style="display:flex;gap:8px;padding:2px 16px 10px;overflow:hidden">{chip("全部", True, 2)}{chip("🍷 Emily", False, 0)}{chip("☕ Cindy", False, 1)}{chip("☕ Coco", False, 1)}</div>'
    + section('🆘 等真人', 2)
    + row6('W','☕','Wei Jie','等 7 分','warm','BMART diploma 是不是 PTPK 可以全额？我 SPM 只有 3 credit 够吗', tag('BMART Diploma','blue')+stage_tag('considering'), state='other', who='佳佳')
    + row6('A','☕','Aina','等 3 分','cool', AINA_Q, tag('1-Day Junior Barista','blue')+stage_tag('curious'))
    + section('已回 · 等客户', 1)
    + row6('S','🍷','Sharon','已回 11:19','cool', SHARON_Q, tag('WNSM 调酒半工读','blue')+stage_tag('hot'), state='mine')
    + link_row('folder', '待确认收款', 1) + link_row('phone', 'IG/FB 给了号码', 2)
    + dock(primary('开始清队列', '· 1 条')))
(OUT/'Queue.dc.html').write_text(phone(queue_inner))

# ══ 7 收款 ══
def bubble_img(caption, t):
    return (f'<div style="display:flex;justify-content:flex-start"><div style="position:relative;width:230px;padding:6px 6px 24px;border-radius:9px;border-top-left-radius:2px;background:{SURF};box-shadow:0 1px 1px rgba(16,24,40,.09)">'
            f'<div style="height:150px;border-radius:6px;background:#eef0f2;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;color:{MUTED};font-size:12px">{ic("image",26,"color:#9aa1ab;")}<span>银行转账截图</span><span class="num" style="font-weight:700;color:{INK2}">RM 1,000.00 · 11:11</span></div>'
            f'<div style="padding:6px 5px 0;font-size:14px">{caption}</div><span class="num" style="position:absolute;right:9px;bottom:5px;font-size:10.5px;color:{TIME}">{t}</span></div></div>')
receipt_card = (f'<div style="margin:0 12px;padding:10px 12px;border-radius:10px;background:{SURF};border:1.5px solid #7a5f18;box-shadow:0 1px 1px rgba(16,24,40,.09)">'
    f'<div style="display:flex;align-items:center;gap:6px;margin-bottom:6px"><span style="font-size:11px;font-weight:700;color:#7a5f18;letter-spacing:.04em">💳 客户付了？</span><span class="num" style="margin-left:auto;padding:1px 7px;border-radius:7px;background:#fdf3c9;color:#7a5f18;font-size:11px;font-weight:700">等了 7 分</span></div>'
    f'<div style="display:grid;grid-template-columns:repeat(3, minmax(0, 1fr));gap:2px 8px;font-size:13px"><div><div style="font-size:11px;color:{MUTED}">课程</div><b>BMART</b></div><div><div style="font-size:11px;color:{MUTED}">应付押金</div><b>RM ___</b></div><div><div style="font-size:11px;color:{MUTED}">图里金额</div><b>RM 1,000</b></div></div></div>')
receipt_inner = (header4('Jason Lim', '☕', 'Cindy 线', 'Bot 已停')
    + ctx4(['BMART Diploma', '中文', '考虑中'], '⚠ 待核付款')
    + stream2([daysep('今天'), bubble_in('好 我先付押金', '11:10'), bubble_img('转好了', '11:11'), bubble_out('收到 Jason 🙏 我让同事核对一下，确认了马上发报名表给你。', '11:11', 'Cindy · Bot')])
    + f'<div style="background:{WARM};padding:0 0 10px">{receipt_card}</div>'
    + f'<div style="border-top:1px solid {LINE};background:{SURF};padding:10px 12px 0;display:flex;flex-direction:column;gap:8px">{big_btn("✅ 确认收款", "Cindy 自动发报名表")}'
    f'<div style="display:grid;grid-template-columns:repeat(2, minmax(0, 1fr));gap:8px"><div style="min-height:42px;display:flex;align-items:center;justify-content:center;border-radius:10px;border:1px solid {LINE};background:{SURF};font-size:13.5px;font-weight:600;color:#c0392b">❌ 不是付款</div><div style="min-height:42px;display:flex;align-items:center;justify-content:center;border-radius:10px;border:1px solid {LINE};background:{SURF};font-size:13.5px;font-weight:600;color:{INK2}">先回一句</div></div></div>'
    + composer4('', '以 Cindy 的身份回复…'))
(OUT/'Receipt.dc.html').write_text(phone(receipt_inner))

# ══ 8 发不出去 · IG（Nurul）══
failed_inner = (header4('Nurul', '☕', 'Coco 线 · IG', 'Bot 已停')
    + ctx4(['BWC Bakery Weekend', 'BM', '考虑中'], '⚠ IG 窗口已关')
    + stream2([daysep('前天'), bubble_in_tr('my number 012-345 6789, boleh call petang. Nak tanya pasal kelas roti weekend tu', '15:10', '我的号码 012-345 6789，下午可以打。想问周末面包课的事'),
               bubble_out('Hai Nurul, boleh! Kelas Bakery Weekend seterusnya 27 Sept. Saya WhatsApp awak sekejap lagi ya 🙂', '16:42', 'Boon', 'failed'),
               fail_card('IG 窗口已关，发不出去', '她留了 WhatsApp 号码，改用：', big_btn(f'{ic("wa",17)}&nbsp;WhatsApp 她 · 012-345 6789'), f'{ic("phone",16)}打电话', '等她再发来')])
    + composer4('', 'IG 现在发不出去'))
(OUT/'Failed.dc.html').write_text(phone(failed_inner, CANVAS))

# ══ 9 发不出去 · WhatsApp（Kelvin）══
failwa_inner = (header4('Kelvin Tan', '☕', 'Cindy 线', 'Bot 已停')
    + ctx4(['FCC 4 日咖啡速成', '中文', '热'], '⚠ WhatsApp 窗口已关')
    + stream2([daysep('前天'), bubble_in('下个月的 4 日班几号开？我要先请假', '09:20'),
               bubble_out('Kelvin 你好，10 月班 13 号开，连续 4 天。名额我先帮你留着，明天前回我就行 👍', '16:02', 'Boon', 'failed'),
               fail_card('WhatsApp 窗口已关，发不出去', '超过 24 小时只能发模板，他一回就能正常聊。', big_btn('发唤醒模板「课程更新」', '这段话存成草稿，他回来一键发'), f'{ic("phone",16)}打电话', '等他再发来')])
    + composer4('', '现在只能发模板'))
(OUT/'FailedWa.dc.html').write_text(phone(failwa_inner, CANVAS))

# ══ 10 登录 ══
def field(label, value):
    return (f'<div style="display:flex;flex-direction:column;gap:5px"><span style="font-size:12px;font-weight:600;color:{MUTED};letter-spacing:.03em">{label}</span>'
            f'<div style="height:46px;padding:0 14px;display:flex;align-items:center;border-radius:10px;background:{SURF2};font-size:15px;color:{INK}">{value}</div></div>')
login_inner = (f'<div style="display:flex;flex-direction:column;gap:18px;padding:80px 24px 0">'
    f'<div><div style="font-size:11.5px;font-weight:700;color:{BRAND};letter-spacing:.08em">JWC ACADEMY</div><h1 style="margin:4px 0 0;font-size:26px;font-weight:700;letter-spacing:-.02em">回复台</h1></div>'
    + field('名字', 'boon') + field('密码', '••••••••')
    + f'<div style="display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:10px;background:{BRAND_SOFT}"><div style="width:40px;height:24px;border-radius:12px;background:{BRAND};position:relative;flex:none"><div style="position:absolute;right:2px;top:2px;width:20px;height:20px;border-radius:50%;background:#ffffff"></div></div><div style="flex:1;font-size:13.5px;color:#1e7a45;font-weight:600">记住这台手机 30 天</div></div>'
    f'<div style="min-height:50px;display:flex;align-items:center;justify-content:center;border-radius:10px;background:{INK};color:#ffffff;font-size:15px;font-weight:700">登录</div></div>')
(OUT/'Login.dc.html').write_text(phone(login_inner))

# ══ 参考页：英文界面（同一屏）══
main_en = (header4('Sharon', '🍷', 'Emily line', 'Bot paused')
    + ctx4(['WNSM Mixology W&amp;S', 'Chinese', 'Hot'])
    + stream2([daysep('Today'), bubble_in('你好 我看到调酒半工读的广告', '11:02'), bubble_out(EMILY_HELLO, '11:02', 'Emily · Bot'),
               bubble_in_tr(SHARON_Q, '11:04', 'Just graduated. If I land a full-time job midway, can I switch to the weekend class? How is the fee counted?')])
    + f'<div style="background:{WARM};padding:0 0 10px">{task4("Can I switch to weekend if I get a job? How is the fee counted?", "Waited 14 min", "hot", "CUSTOMER ASKED")}</div>'
    + drafts4([draft4('Yes, can switch · fee prorated', BOON_REPLY, 'EN: Yes, switch anytime; fee prorated by remaining lessons. Free trial Sat 2pm, hold a seat?'),
               draft4('Ask first: job-hunting or full-time study', 'Sharon 你好，想先了解一下：你是想边找工作边学，还是先专心学完 9 个月？两种情况推荐的班不一样。', 'EN: Job-hunting while studying, or full-time? Different class fits.')], 'DRAFTS', 'More')
    + composer4('', 'Reply as Emily… (sent in 中文)', focused=True))
(OUT/'MainEn.dc.html').write_text(phone(main_en))

# ══ canvas：两页 ══
W,H,G = 390,844,80
def x(i): return i*(W+G)
R2 = 1300
boards = [
    {"file":"Notify.dc.html",  "x":x(0),"y":0,  "w":W,"h":200,"title":"0 · 通知","page":"v4"},
    {"file":"Login.dc.html",   "x":x(0),"y":300,"w":W,"h":H,"title":"10 · 登录（第一次装才看到）","page":"v4"},
    {"file":"Main.dc.html",    "x":x(1),"y":0,  "w":W,"h":H,"title":"1 · 会话 · 回客户","page":"v4"},
    {"file":"Reply.dc.html",   "x":x(2),"y":0,  "w":W,"h":H,"title":"2 · 马来文客户 · 自动翻译","page":"v4"},
    {"file":"Gate.dc.html",    "x":x(3),"y":0,  "w":W,"h":H,"title":"3 · 从队列进来 · 先停 bot","page":"v4"},
    {"file":"Sent.dc.html",    "x":x(4),"y":0,  "w":W,"h":H,"title":"4 · 发完","page":"v4"},
    {"file":"Queue.dc.html",   "x":x(0),"y":R2, "w":W,"h":H,"title":"5 · 待回","page":"v4"},
    {"file":"Quick.dc.html",   "x":x(1),"y":R2, "w":W,"h":H,"title":"6 · 话术","page":"v4"},
    {"file":"Receipt.dc.html", "x":x(2),"y":R2, "w":W,"h":H,"title":"7 · 收款截图","page":"v4"},
    {"file":"Failed.dc.html",  "x":x(3),"y":R2, "w":W,"h":H,"title":"8 · 发不出去 · IG","page":"v4"},
    {"file":"FailedWa.dc.html","x":x(4),"y":R2, "w":W,"h":H,"title":"9 · 发不出去 · WhatsApp","page":"v4"},
    {"file":"TelegramReply.dc.html","x":x(0),"y":0,"w":W,"h":660,"title":"备选 · Telegram 里直接回（零安装）","page":"ref"},
    {"file":"MainEn.dc.html",  "x":x(1),"y":0,  "w":W,"h":H,"title":"参考 · 英文界面（同一屏）","page":"ref"},
    {"file":"SentMeta.dc.html","x":x(2),"y":0,  "w":W,"h":360,"title":"参考 · 发完提示按渠道","page":"ref"},
]
notes = [
    {"id":"v4-what","x":x(1),"y":-180,"w":900,"page":"v4","text":"v4 · 员工看到的就是这 11 屏。平时只用 0 → 1 → 4：通知点开、回、发完。2/3/6/7/8/9 是遇到才出现的情况。10 只在第一次装手机时出现。\n界面上不再出现接口名、规则、开关；那些在第二页「参考」。人名、消息、价格都是示例。"},
    {"id":"ref-rules","x":x(0),"y":-300,"w":1300,"page":"ref","text":"不进界面、但要定的规则（Lucas 已定的打 ✓）：\n✓ SOS 任何值班的人都能接，先点先得；认领后保留在队列直到第一条人工回复。\n· WhatsApp：人回过后 12 小时没动静 Bot 接回（需开 PAUSE_AUTO_RESUME=1，否则提示改成「Bot 不会自动回来」）。IG/FB：人回过后 Bot 永久让位。\n· 人接手时以线的人设（Emily / Cindy / Coco）回复，自己的名字只在内部记录。\n· 主号和桥接线不进 app，那些在各自 WhatsApp 里回。\n· 上线前验证：暂停 bot 后排好的唤醒模板停不停。\n后端要做的（按重要性）：值班状态 + 我认领的 SOS 跨线放行 · 认领不立刻关闭 · 每台设备独立长期令牌，SOS 签名链接兼作登录 · 翻译 · AI 草稿只用 Sheet 目录事实 · dashboard 客户行显示「X 在回」 · Telegram v0 带按钮原文照发。收款确认、模板重发、话术、接管都是现有接口。"},
]
canvas = {"pages":[{"id":"v4","name":"给员工看的"},{"id":"ref","name":"参考 · 不进界面"}], "artboards":boards, "annotations":notes, "launch":{"view":"canvas","page":"v4"}}
(OUT/'canvas.json').write_text(json.dumps(canvas, ensure_ascii=False, indent=2))
print(len(boards), 'boards')
