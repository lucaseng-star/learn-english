# v3 —— 并入第二轮盲点九条。先跑 v2 生成器（它自己会跑 v1 并存档），把 v2 八块复制成 V2* 存档，再画 v3。
import json, pathlib, shutil
SCR = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(__file__).resolve().parent
v2ns = {'__file__': str(SCR / 'build_v2.py'), '__name__': 'v2'}
exec((SCR / 'build_v2.py').read_text(), v2ns)
g = globals()
for k in ['INK','INK2','MUTED','TIME','LINE','LINE_SOFT','SURF','SURF2','CANVAS','BRAND','BRAND_SOFT','ACCENT','WARM','LINK','TICK','TAG','WAIT','STAGE',
          'ic','phone','iconbtn','tag','stage_tag','wait_pill','avatar','chip','section','primary','dock','bubble_in','bubble_out','daysep','stream',
          'header2','st','ctxline','task_card','draft_card','drafts_row','composer2','bubble_in_tr','stream2','sos_marker2','scrim','recent_chip','qrow2',
          'SHARON_Q','AINA_Q','AINA_TASK']:
    g[k] = v2ns[k]
HEAD, TAIL = v2ns['ns']['HEAD'], v2ns['ns']['TAIL']
v2_canvas = json.loads((OUT / 'canvas.json').read_text())

# ── v2 存档：复制成 V2*（内容不变，页面换到 v2）──
V2 = {'Notify':'V2Notify','Main':'V2Main','Reply':'V2Reply','Gate':'V2Gate','Sent':'V2Sent','Quick':'V2Quick','Queue':'V2Queue','Failed':'V2Failed'}
for old, new in V2.items():
    shutil.copyfile(OUT / f'{old}.dc.html', OUT / f'{new}.dc.html')

# ══════════ 0 · Notify（v3：发给值班的人）══════════
notify = (f'<div style="width:390px;height:280px;background:{CANVAS};display:flex;flex-direction:column;gap:10px;padding:16px;box-sizing:border-box;font-size:15px;line-height:1.45">'
    f'<div style="font-size:11.5px;font-weight:700;color:{MUTED};letter-spacing:.06em">推送 · 只发给今天值班的人</div>'
    f'<div style="display:flex;gap:11px;padding:12px 14px;border-radius:14px;background:{SURF};box-shadow:0 1px 2px rgba(16,24,40,.05), 0 8px 24px rgba(16,24,40,.10)">'
    f'<div style="width:38px;height:38px;flex:none;border-radius:10px;background:{BRAND};color:#ffffff;display:flex;align-items:center;justify-content:center">{ic("bolt",20,"color:#ffffff;","2")}</div>'
    f'<div style="flex:1;min-width:0"><div style="display:flex;align-items:baseline;gap:6px"><span style="font-size:14.5px;font-weight:700">🆘 Sharon 等真人 <span class="num" style="color:#c0392b">14 分</span></span><span class="num" style="margin-left:auto;font-size:11.5px;color:{TIME}">11:18</span></div>'
    f'<div style="font-size:13.5px;line-height:1.4;color:{INK2};margin-top:2px">🍷 Emily 线 · 问：刚毕业。如果中途找到全职工作可以转周末班吗？学费怎么算？</div>'
    f'<div style="font-size:12px;color:{MUTED};margin-top:4px">值班：你、佳佳 · 先点先得。点开 = 认领 + 停 bot + 键盘弹出；佳佳先点了会显示「佳佳 已接」。</div></div></div>'
    f'<div style="display:flex;align-items:center;gap:8px;font-size:12.5px;color:{MUTED}">{ic("chevron",14,"color:#9aa1ab;transform:rotate(90deg);","2")}<span>已经登录的手机：落在「1 · 会话」；没登录：先落「11 · 登录」，链接自带签名，确认即登录</span></div></div>')
(OUT/'Notify.dc.html').write_text(HEAD + notify + TAIL)

# ══════════ 0b · Telegram 直接回（零安装 v0，390×600）══════════
def tg_bubble(html, mine=False):
    bg = ACCENT if mine else SURF
    just = 'flex-end' if mine else 'flex-start'
    return f'<div style="display:flex;justify-content:{just}"><div style="max-width:92%;padding:9px 12px;border-radius:12px;background:{bg};box-shadow:0 1px 1px rgba(16,24,40,.09);font-size:13.5px;line-height:1.45;white-space:pre-wrap">{html}</div></div>'
def tg_btn(label, primary_=False):
    st_ = f'background:{BRAND};color:#ffffff' if primary_ else f'background:{SURF2};color:{INK}'
    return f'<div style="flex:1;min-height:36px;display:flex;align-items:center;justify-content:center;border-radius:9px;font-size:13px;font-weight:700;{st_}">{label}</div>'
tg = (f'<div style="width:390px;height:660px;background:{CANVAS};display:flex;flex-direction:column;box-sizing:border-box;font-size:15px;line-height:1.45">'
    f'<div style="display:flex;align-items:center;gap:8px;padding:12px 16px;border-bottom:1px solid {LINE};background:{SURF}"><div style="width:32px;height:32px;border-radius:50%;background:{INK};color:#ffffff;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700">JWC</div><div><div style="font-size:14px;font-weight:700">🤖 Bot 值班</div><div style="font-size:11.5px;color:{MUTED}">Telegram 群 · 现有告警频道</div></div><span style="margin-left:auto;font-size:11px;font-weight:700;color:{MUTED};letter-spacing:.06em">零安装 V0</span></div>'
    f'<div style="flex:1;display:flex;flex-direction:column;gap:10px;padding:12px 12px;overflow:hidden">'
    + tg_bubble('🆘 客人在等真人回答\n📱 +60 12-345 6788\n🙋 Sharon\n📚 WNSM 调酒半工读\n❓ 刚毕业。如果中途找到全职工作可以转周末班吗？学费怎么算？\nℹ️ Emily 已跟他说「5-10 分钟真人回你」\n<span style="color:#7b838e">11:04 · 发给值班：Boon、佳佳</span>'
                + f'<div style="display:flex;gap:6px;margin-top:8px">{tg_btn("我接 · 在这里回", True)}{tg_btn("打开 app 回")}</div>')
    + tg_bubble('✅ Boon 已接（11:18）。Bot 已停。\n直接回覆这条消息，我以 <b>Emily</b> 的名义原文发给 Sharon。', False)
    + tg_bubble('可以的 Sharon，半工读转周末班随时可以，学费按剩余堂数折算，不会重复收。刚毕业的话建议先来看一堂实操（免费），这周六 2 点有一场，帮你留位？', True)
    + tg_bubble('✓✓ 已发给 Sharon（Emily）· 11:19\n12 小时没动静 Bot 接回。要现在交还回 <b>/bot 6788</b>', False)
    + '</div>'
    + f'<div style="padding:10px 16px 14px;border-top:1px solid {LINE};background:{SURF};font-size:12px;line-height:1.45;color:{MUTED}">现有 <b>/answer</b> 是「刚跟经理 confirm 好了 😊 + 答案」的包装；v0 只改成原文照发、带按钮。先用它量 SOS → 首回时间，app 只在 v0 不够用时才做。</div></div>')
(OUT/'TelegramReply.dc.html').write_text(HEAD + tg + TAIL)

# ══════════ 6 · Queue（v3：值班、只有 AI 线、认领状态）══════════
def qrow3(initial, emoji, name, wait, level, question, tags_html, state='open', who='', extra=''):
    if state == 'mine':
        right = f'<div style="align-self:center;padding:5px 9px;border-radius:7px;background:{BRAND};color:#ffffff;font-size:11.5px;font-weight:700;white-space:nowrap;text-align:center;line-height:1.3">你在回<br><span style="font-weight:500;opacity:.85">{extra}</span></div>'; op=''; bg=SURF
    elif state == 'other':
        right = f'<div style="align-self:center;padding:5px 9px;border-radius:7px;background:{SURF2};color:{MUTED};font-size:11.5px;font-weight:700;white-space:nowrap;text-align:center;line-height:1.3">{who} 在回<br><span style="font-weight:500">{extra}</span></div>'; op='opacity:.55;'; bg=SURF
    else:
        right = f'<div style="align-self:center;width:44px;height:44px;display:flex;align-items:center;justify-content:center;border-radius:10px;background:{SURF2};color:{INK}">{ic("bolt",19)}</div>'; op=''; bg=BRAND_SOFT
    return (f'<div style="display:grid;grid-template-columns:42px minmax(0,1fr) auto;gap:11px;align-items:start;padding:12px 12px 12px 16px;border-bottom:1px solid {LINE_SOFT};background:{bg};{op}">'
            f'{avatar(initial, emoji)}<div style="min-width:0;display:flex;flex-direction:column;gap:3px">'
            f'<div style="display:flex;align-items:baseline;gap:8px"><span style="flex:1;min-width:0;font-size:15px;font-weight:600;letter-spacing:-.01em;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{name}</span>{wait_pill(wait, level)}</div>'
            f'<p style="margin:0;font-size:13.5px;line-height:1.38;color:{MUTED};display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden">{question}</p>'
            f'<div style="display:flex;flex-wrap:wrap;gap:5px;margin-top:3px">{tags_html}</div></div>{right}</div>')
def link_row(icon, label, count):
    return f'<div style="display:flex;align-items:center;gap:8px;padding:12px 16px;border-top:1px solid {LINE_SOFT};font-size:14px;font-weight:600;color:{INK}">{ic(icon,18,"color:#3c444e;")}<span style="flex:1">{label}</span><span class="num" style="color:{BRAND}">{count}</span>{ic("chevron",16,"color:#9aa1ab;","2")}</div>'
queue_inner = (f'<div style="display:flex;align-items:center;gap:8px;padding:16px 8px 4px 16px"><h1 style="margin:0;font-size:21px;font-weight:700;letter-spacing:-.015em">待回</h1><span style="flex:1"></span>'
    f'<div style="display:flex;align-items:center;gap:6px;height:32px;padding:0 10px 0 8px;border-radius:999px;background:{BRAND_SOFT};color:#1e7a45;font-size:12.5px;font-weight:700"><span style="width:8px;height:8px;border-radius:50%;background:{BRAND}"></span>值班中</div>{iconbtn("gear")}</div>'
    f'<div style="padding:0 16px 8px;font-size:12.5px;color:{MUTED}">今天值班：<b style="color:{INK2}">你、佳佳</b> · SOS 任何值班的人都能接，先点先得</div>'
    f'<div style="display:flex;gap:8px;padding:2px 16px 10px;overflow:hidden">{chip("全部 AI 线", True, 3)}{chip("🍷 Emily", False, 1)}{chip("☕ Cindy", False, 1)}{chip("☕ Coco", False, 1)}</div>'
    + section('🆘 等真人', 3, '最久没回的在最上')
    + qrow3('S','🍷','Sharon','已回 11:19','cool', SHARON_Q, tag('WNSM 调酒半工读','blue')+stage_tag('hot'), state='mine', extra='等客户回')
    + qrow3('W','☕','Wei Jie','等 7 分','warm','BMART diploma 是不是 PTPK 可以全额？我 SPM 只有 3 credit 够吗', tag('BMART Diploma','blue')+stage_tag('considering'), state='other', who='佳佳', extra='认领 6 分 · 还没回')
    + qrow3('A','☕','Aina','等 3 分','cool', AINA_Q, tag('1-Day Junior Barista (BM/EN)','blue')+stage_tag('curious'))
    + link_row('folder', '待确认收款', 1) + link_row('phone', 'IG/FB 给了号码，等你打', 2)
    + f'<div style="padding:10px 16px 0;font-size:12px;line-height:1.45;color:{MUTED}">主号和桥接线（Boon、佳佳、Lisa、Saturnbird、Amie 的 WhatsApp）不在这里：那些本来就在各自的 WhatsApp 里回。</div>'
    + dock(primary('开始清队列', '· 1 条待认领')))
(OUT/'Queue.dc.html').write_text(phone(queue_inner))

# ══════════ 9 · Receipt 付款截图（Wei Jie · Cindy 线）══════════
def bubble_img(caption, t):
    return (f'<div style="display:flex;justify-content:flex-start"><div style="position:relative;width:230px;padding:6px 6px 24px;border-radius:9px;border-top-left-radius:2px;background:{SURF};box-shadow:0 1px 1px rgba(16,24,40,.09)">'
            f'<div style="height:150px;border-radius:6px;background:#eef0f2;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;color:{MUTED};font-size:12px">{ic("image",26,"color:#9aa1ab;")}<span>银行转账截图</span><span class="num" style="font-weight:700;color:{INK2}">RM 1,000.00 · 13:39</span></div>'
            f'<div style="padding:6px 5px 0;font-size:14px">{caption}</div><span class="num" style="position:absolute;right:9px;bottom:5px;font-size:10.5px;color:{TIME}">{t}</span></div></div>')
receipt_task = (f'<div style="margin:0 12px;padding:10px 12px;border-radius:10px;background:{SURF};border:1.5px solid #7a5f18;box-shadow:0 1px 1px rgba(16,24,40,.09)">'
    f'<div style="display:flex;align-items:center;gap:6px;margin-bottom:4px"><span style="font-size:11px;font-weight:700;color:#7a5f18;letter-spacing:.04em">💳 客户付了？要人眼看</span><span class="num" style="margin-left:auto;padding:1px 7px;border-radius:7px;background:#fdf3c9;color:#7a5f18;font-size:11px;font-weight:700">等了 6 分</span></div>'
    f'<div style="display:grid;grid-template-columns:repeat(2, minmax(0, 1fr));gap:2px 12px;font-size:13px"><div><span style="color:{MUTED}">课程</span> BMART Diploma</div><div><span style="color:{MUTED}">应付</span> 押金 RM ___</div><div><span style="color:{MUTED}">图里金额</span> <b>RM 1,000</b></div><div><span style="color:{MUTED}">收款账号</span> 只认 JWC 官方</div></div></div>')
receipt_inner = (header2('Wei Jie', '☕', 'Cindy 线', st('你在回','green') + st('Bot 已停','green') + st('对客户显示 Cindy','gray'))
    + ctxline(['BMART Diploma', '中文', '考虑中'], '⚠ 待核付款')
    + stream2([daysep('今天'), bubble_in('好 我先付押金', '13:38'), bubble_img('转好了', '13:39'),
               bubble_out('收到 Wei Jie 🙏 我让同事核对一下，确认了马上发报名表给你。', '13:39', 'Cindy · Bot'),
               f'<div style="display:flex;justify-content:center"><div style="max-width:92%;padding:8px 12px;border-radius:10px;background:#fdf3c9;color:#7a5f18;font-size:12.5px;font-weight:600;line-height:1.4;text-align:center">💳 Bot 判断是付款截图，没有自己确认（规则：只有人能确认收款）· 13:39</div></div>'])
    + f'<div style="background:{WARM};padding:0 0 10px">{receipt_task}</div>'
    + f'<div style="border-top:1px solid {LINE};background:{SURF};padding:10px 12px 0;display:flex;flex-direction:column;gap:8px">'
    f'<div style="min-height:48px;display:flex;flex-direction:column;align-items:center;justify-content:center;border-radius:10px;background:{BRAND};color:#ffffff;font-size:15px;font-weight:700;line-height:1.2">✅ 确认收款<span style="font-size:11.5px;font-weight:500;opacity:.85;margin-top:2px">Cindy 自动发报名表 + 课前须知</span></div>'
    f'<div style="display:grid;grid-template-columns:repeat(2, minmax(0, 1fr));gap:8px"><div style="min-height:42px;display:flex;align-items:center;justify-content:center;border-radius:10px;border:1px solid {LINE};background:{SURF};font-size:13.5px;font-weight:600;color:#c0392b">❌ 不是付款 / 图不清</div><div style="min-height:42px;display:flex;align-items:center;justify-content:center;border-radius:10px;border:1px solid {LINE};background:{SURF};font-size:13.5px;font-weight:600;color:{INK2}">先回一句</div></div></div>'
    + composer2('', '以 Cindy 的身份回复…'))
(OUT/'Receipt.dc.html').write_text(phone(receipt_inner))

# ══════════ 10 · FailedWa WhatsApp 24 小时窗口（Kelvin · Cindy 线）══════════
failwa_inner = (header2('Kelvin Tan', '☕', 'Cindy 线', st('你在回','green') + st('Bot 已停','green') + st('对客户显示 Cindy','gray'))
    + ctxline(['FCC 4 日咖啡速成', '中文', '热'], '⚠ WhatsApp 24 小时窗口已关')
    + stream2([daysep('前天'), bubble_in('下个月的 4 日班几号开？我要先请假', '09:20'),
               bubble_out('Kelvin 你好，10 月班 13 号开，连续 4 天。名额我先帮你留着，明天前回我就行 👍', '16:02', 'Boon · 人手（客户看到的是 Cindy）', 'failed'),
               f'<div style="margin:0 2px;padding:12px;border-radius:10px;background:{SURF};border:1.5px solid #c0392b">'
               f'<div style="display:flex;align-items:center;gap:6px;font-size:13.5px;font-weight:700;color:#c0392b">❌ 没发出去：WhatsApp 24 小时窗口已关</div>'
               f'<div style="margin-top:3px;font-size:12.5px;line-height:1.4;color:{INK2}">客户上次发言 前天 09:20。超过 24 小时只能发 Meta 审核过的模板；他一回，窗口重开，就能正常聊。</div>'
               f'<div style="display:flex;flex-direction:column;gap:6px;margin-top:10px">'
               f'<div style="min-height:42px;display:flex;flex-direction:column;align-items:center;justify-content:center;border-radius:10px;background:{BRAND};color:#ffffff;font-size:14px;font-weight:700;line-height:1.2">发唤醒模板「课程更新」<span style="font-size:11.5px;font-weight:500;opacity:.85;margin-top:2px">按 Cindy 的模板发，参数已填好</span></div>'
               f'<div style="display:grid;grid-template-columns:repeat(2, minmax(0, 1fr));gap:6px">'
               f'<div style="min-height:40px;display:flex;align-items:center;justify-content:center;gap:6px;border-radius:10px;border:1px solid {LINE};background:{SURF};font-size:13.5px;font-weight:600;color:{INK2}">{ic("phone",16)}打电话 017-654 3210</div>'
               f'<div style="min-height:40px;display:flex;align-items:center;justify-content:center;border-radius:10px;border:1px solid {LINE};background:{SURF};font-size:13.5px;font-weight:600;color:{INK2}">等他再发来</div></div></div></div>'])
    + f'<div style="display:flex;align-items:center;gap:8px;padding:9px 12px;border-top:1px solid {LINE};background:{SURF};font-size:12.5px;color:{MUTED}">{ic("info",15,"color:#7b838e;","2")}这段话会存成草稿，他一回来就能一键发出。</div>'
    + composer2('', 'WhatsApp 这边现在只能发模板'))
(OUT/'FailedWa.dc.html').write_text(phone(failwa_inner, CANVAS))

# ══════════ 11 · Login 登录与设备 ══════════
def field(label, value, placeholder=False):
    return (f'<div style="display:flex;flex-direction:column;gap:5px"><span style="font-size:12px;font-weight:600;color:{MUTED};letter-spacing:.03em">{label}</span>'
            f'<div style="height:46px;padding:0 14px;display:flex;align-items:center;border-radius:10px;background:{SURF2};font-size:15px;color:{TIME if placeholder else INK}">{value}</div></div>')
login_inner = (f'<div style="display:flex;flex-direction:column;gap:18px;padding:64px 24px 0">'
    f'<div><div style="font-size:11.5px;font-weight:700;color:{BRAND};letter-spacing:.08em">JWC ACADEMY</div><h1 style="margin:4px 0 0;font-size:26px;font-weight:700;letter-spacing:-.02em">回复台</h1><div style="margin-top:4px;font-size:13.5px;color:{MUTED}">和 dashboard 同一个账号密码</div></div>'
    + field('名字', 'boon') + field('密码', '••••••••')
    + f'<div style="display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:10px;background:{BRAND_SOFT}"><div style="width:40px;height:24px;border-radius:12px;background:{BRAND};position:relative;flex:none"><div style="position:absolute;right:2px;top:2px;width:20px;height:20px;border-radius:50%;background:#ffffff"></div></div><div style="flex:1;font-size:13.5px;line-height:1.35;color:#1e7a45"><b>记住这台手机 30 天</b><br><span style="color:#3c7a55">从通知点进来不用再登录。手机丢了在 dashboard「设备」里让它下线。</span></div></div>'
    f'<div style="min-height:50px;display:flex;align-items:center;justify-content:center;border-radius:10px;background:{INK};color:#ffffff;font-size:15px;font-weight:700">登录</div>'
    f'<div style="display:flex;align-items:center;gap:10px;color:{TIME};font-size:12px"><span style="flex:1;height:1px;background:{LINE}"></span>或<span style="flex:1;height:1px;background:{LINE}"></span></div>'
    f'<div style="display:flex;gap:10px;padding:12px;border-radius:10px;border:1px solid {LINE};background:{SURF}">{ic("clip",20,"color:#3c444e;flex:none;margin-top:2px;")}<div style="font-size:13.5px;line-height:1.4;color:{INK2}"><b>从 Telegram 或邮件点进来的 SOS 链接自带签名</b><br><span style="color:{MUTED}">和现有认领链接同一套。点一下：确认「你是 Boon？」，就登录并落在那个会话。</span></div></div>'
    + '</div>'
    + f'<div style="margin-top:auto;padding:0 24px 28px;font-size:12px;line-height:1.45;color:{MUTED}">现在 dashboard 的密钥放在 sessionStorage，关掉就没了；手机上会每次重新登录。这一屏要靠后端给每台设备发独立的长期令牌，并能单独作废。</div>')
(OUT/'Login.dc.html').write_text(phone(login_inner))

# ══════════ 1b · MainEn 英文界面（同一屏，Lisa 视角）══════════
main_en = (header2('Sharon', '🍷', 'Emily line', st('On it','green') + st('Bot paused','green') + st('Shows as Emily','gray'))
    + (f'<div style="display:flex;align-items:center;gap:6px;padding:7px 16px;border-bottom:1px solid {LINE_SOFT};background:{SURF};font-size:12.5px;color:{INK2};white-space:nowrap;overflow:hidden">'
       f'<span style="font-weight:600">WNSM Mixology W&amp;S</span><span style="color:{TIME}">·</span><span style="font-weight:600">Chinese</span><span style="color:{TIME}">·</span><span style="font-weight:600">Hot</span><span style="color:{TIME}">·</span><span style="color:{TIME}">No landmines</span>'
       f'<span style="margin-left:auto;color:{TIME}">{ic("chevron",14,"color:#9aa1ab;transform:rotate(90deg);","2")}</span></div>')
    + stream2([daysep('Today'), bubble_in('你好 我看到调酒半工读的广告', '11:02'),
               bubble_out('哈喽 Sharon，我是 Emily 🍷 调酒半工读是 9 个月 36 堂，一周上 1 天课，其余时间在合作酒吧带薪实习。你现在是在工作，还是刚毕业？', '11:02', 'Emily · Bot'),
               bubble_in_tr(SHARON_Q, '11:04', 'Just graduated. If I land a full-time job midway, can I switch to the weekend class? How is the fee counted?')])
    + (f'<div style="background:{WARM};padding:0 0 10px"><div style="margin:0 12px;padding:10px 12px;border-radius:10px;background:{SURF};border:1.5px solid #c0392b;box-shadow:0 1px 1px rgba(16,24,40,.09)">'
       f'<div style="display:flex;align-items:center;gap:6px;margin-bottom:4px"><span style="font-size:11px;font-weight:700;color:#c0392b;letter-spacing:.04em">🆘 CUSTOMER ASKED</span><span class="num" style="margin-left:auto;padding:1px 7px;border-radius:7px;background:#fdecea;color:#c0392b;font-size:11px;font-weight:700">Waited 14 min · promised 5-10</span></div>'
       f'<div style="font-size:14.5px;font-weight:600;line-height:1.4;color:{INK}">Can I switch to weekend if I get a job? How is the fee counted? <span style="font-weight:500;color:{MUTED}">· original 中文</span></div></div></div>')
    + f'<div style="border-top:1px solid {LINE};background:{SURF}">'
    + (f'<div style="display:flex;align-items:center;gap:6px;padding:8px 12px 0;font-size:11.5px;font-weight:700;color:{MUTED};letter-spacing:.04em">{ic("asterisk",13,"color:#7b838e;")}DRAFTS · CATALOG FACTS ONLY<span style="margin-left:auto;padding:4px 10px;border-radius:999px;background:{SURF2};color:{INK};font-size:12px;font-weight:700;letter-spacing:0">More</span></div>'
       f'<div style="display:flex;gap:8px;padding:8px 12px 0;overflow:hidden">'
       + draft_card('Yes, can switch · fee prorated', '可以的 Sharon，半工读转周末班随时可以，学费按剩余堂数折算，不会重复收。刚毕业的话建议先来看一堂实操（免费），这周六 2 点有一场，帮你留位？', 'Catalog ✓', 286, 'EN: Yes, switch anytime; fee prorated by remaining lessons. Free trial class Sat 2pm, hold a seat?')
       + draft_card('Ask first: job-hunting or full-time study', 'Sharon 你好，想先了解一下：你是想边找工作边学，还是先专心学完 9 个月？两种情况推荐的班不一样。', 'No price', 286, 'EN: Are you job-hunting while studying, or studying full-time? Different class fits.')
       + '</div>')
    + composer2('', 'Reply as Emily… (sent in 中文)', focused=True) + '</div>')
(OUT/'MainEn.dc.html').write_text(phone(main_en))

# ══════════ 4b · SentMeta 发完之后 · 按渠道（390×360）══════════
def toast_strip(text_html, btn):
    return (f'<div style="display:flex;align-items:center;gap:8px;padding:9px 12px;border:1px solid {LINE};border-radius:10px;background:{SURF};font-size:13px;color:{INK2}">'
            f'{ic("check2",16,"color:#2ec06a;","2.2")}<span style="flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{text_html}</span>'
            f'<span style="flex:none;padding:6px 10px;border-radius:999px;background:{SURF2};font-size:12.5px;font-weight:700;color:{INK};white-space:nowrap">{btn}</span></div>')
sentmeta = (f'<div style="width:390px;height:360px;background:{CANVAS};display:flex;flex-direction:column;gap:10px;padding:16px;box-sizing:border-box;font-size:15px;line-height:1.45">'
    f'<div style="font-size:11.5px;font-weight:700;color:{MUTED};letter-spacing:.06em">发完之后 · 同一行提示，按渠道两种话</div>'
    f'<div style="font-size:12.5px;font-weight:700;color:{INK2}">WhatsApp 线（Emily / Cindy / Coco）</div>'
    + toast_strip(f'<span style="font-weight:600">已发 ✓✓ · SOS 已解决</span><span style="color:{MUTED}"> · 12 小时没动静 Bot 接回</span>', '🟢 交还')
    + f'<div style="font-size:12px;line-height:1.4;color:{MUTED}">「12 小时接回」要 <b>PAUSE_AUTO_RESUME=1</b> 才是真的；现在生产上多半只报名单不放回。上线前二选一：开开关，或把这句改成「Bot 不会自动回来」。</div>'
    f'<div style="font-size:12.5px;font-weight:700;color:{INK2};margin-top:4px">IG / FB</div>'
    + toast_strip(f'<span style="font-weight:600">已发 ✓✓</span><span style="color:{MUTED}"> · 已转人手，Bot 不会自动回来</span>', '🟢 让 Bot 接管')
    + f'<div style="font-size:12px;line-height:1.4;color:{MUTED}">代码现状：IG/FB 同事一开口就 humanOnly，永久让位，自动放回明确不碰它。所以这里不能写 12 小时。</div></div>')
(OUT/'SentMeta.dc.html').write_text(HEAD + sentmeta + TAIL)

# ══════════ canvas.json：三页 ══════════
W,H,G = 390,844,80
def x(i): return i*(W+G)
R2, R3 = 1160, 2200
v3_boards = [
    {"file":"Notify.dc.html",       "x":x(0),"y":0,   "w":W,"h":280,"title":"0 · 通知 → 直达（值班）","page":"v3"},
    {"file":"TelegramReply.dc.html","x":x(0),"y":360, "w":W,"h":660,"title":"0b · Telegram 直接回 · 零安装 v0","page":"v3"},
    {"file":"Main.dc.html",         "x":x(1),"y":0,   "w":W,"h":H,"title":"1 · 会话（从通知进来）","page":"v3"},
    {"file":"MainEn.dc.html",       "x":x(2),"y":0,   "w":W,"h":H,"title":"1b · 同一屏 · 英文界面","page":"v3"},
    {"file":"Reply.dc.html",        "x":x(3),"y":0,   "w":W,"h":H,"title":"2 · 翻译内建 + 草稿写答案","page":"v3"},
    {"file":"Gate.dc.html",         "x":x(4),"y":0,   "w":W,"h":H,"title":"3 · 从队列进来 · 先停 bot","page":"v3"},
    {"file":"Queue.dc.html",        "x":x(0),"y":R2,  "w":W,"h":H,"title":"6 · 队列 · 值班 · 谁在回","page":"v3"},
    {"file":"Quick.dc.html",        "x":x(1),"y":R2,  "w":W,"h":H,"title":"5 · 话术先搜索 · 插入前预览","page":"v3"},
    {"file":"Sent.dc.html",         "x":x(2),"y":R2,  "w":W,"h":H,"title":"4 · 发完一行提示（WhatsApp）","page":"v3"},
    {"file":"SentMeta.dc.html",     "x":x(3),"y":R2,  "w":W,"h":360,"title":"4b · 发完之后 · 按渠道","page":"v3"},
    {"file":"Receipt.dc.html",      "x":x(4),"y":R2,  "w":W,"h":H,"title":"9 · 付款截图 · 确认收款","page":"v3"},
    {"file":"Failed.dc.html",       "x":x(0),"y":R3,  "w":W,"h":H,"title":"7 · 送不出去 · IG 窗口","page":"v3"},
    {"file":"FailedWa.dc.html",     "x":x(1),"y":R3,  "w":W,"h":H,"title":"10 · 送不出去 · WhatsApp 窗口 → 模板","page":"v3"},
    {"file":"Login.dc.html",        "x":x(2),"y":R3,  "w":W,"h":H,"title":"11 · 登录与设备","page":"v3"},
]
v2_boards = []
for b in v2_canvas['artboards']:
    if b.get('page') == 'v2':
        stem = b['file'].replace('.dc.html','')
        b2 = dict(b); b2['file'] = V2[stem] + '.dc.html'; b2['title'] = 'v2 · ' + b.get('title', stem); v2_boards.append(b2)
v1_boards = [b for b in v2_canvas['artboards'] if b.get('page') == 'v1']
old_notes = v2_canvas.get('annotations', [])
v3_notes = [
    {"id":"v3-rules","x":x(0),"y":-560,"w":700,"page":"v3","text":"v3 · 你定的规则：SOS 任何值班的人都能接。\n落法：\n· 「值班」是一个开关（画板 6 右上）。开着才收 SOS 推送、才出现在「今天值班」名单。\n· 值班的人对任何 AI 线的 SOS 都能认领、回复；认领之后那条会话对认领人开放，跨线守卫只放行「我认领的 SOS」，别的客人照旧看不到。\n· 先点先得不变，第二个点的人看到「佳佳 已接」。\n· 认领后 SOS 不再立刻从队列消失：保留到第一条人工回复发出（或手动解决），期间队列显示「佳佳 在回 · 认领 6 分 · 还没回」。dashboard 的客户列表也要显示同一个标签，不然桌面的人看不到手机上谁认领了。"},
    {"id":"v3-map","x":x(0)+760,"y":-560,"w":760,"page":"v3","text":"九条盲点 → 画板：\n① 谁能回哪条线 → 规则见左，画板 6 值班开关、0 通知只发值班的人\n② 真人线已在 WhatsApp 里回 → 画板 6 去掉「主号未回」；app 只管三条 AI 线 + IG/FB + 收款\n③ Telegram 直接回 → 画板 0b：零安装 v0，先用它量 SOS→首回时间\n④ IG/FB 永久让位、12 小时要开关 → 画板 4b 两种提示\n⑤ 认领后的状态 → 画板 6「在回 · 还没回」+ 规则见左\n⑥ 付款截图 → 画板 9：只有人能确认收款，确认后 bot 自动发报名表（现有 /verify /reject）\n⑦ 界面语言 → 画板 1b：同一屏英文（dashboard 已有 59 处 i18n，沿用）\n⑧ 登录态 → 画板 11：记住设备 30 天 + 签名链接即登录 + 设备下线\n⑨ WhatsApp 24 小时窗口 → 画板 10：只能发审核过的模板\n上线前必须验证：人接管暂停 bot 后，排好的唤醒模板到底停不停。"},
    {"id":"v3-backend","x":x(0)+1560,"y":-560,"w":560,"page":"v3","text":"确认后要动后端的（照重要性）：\n1. 值班状态 + 「我认领的 SOS」跨线放行\n2. 认领不立刻关闭 open；加「已回」时间\n3. 每台设备独立长期令牌，可单独作废；SOS 签名链接兼作登录\n4. 翻译：进来 BM/EN→中文，出去中文→客户语言\n5. AI 草稿：只准用 Sheet 目录事实\n6. dashboard 客户行显示「X 在回」\n7. Telegram v0：SOS 消息带按钮，回覆原文照发\n其它（收款确认、模板重发、话术、接管）都是现有接口。人名、消息、价格皆示例。"},
    {"id":"v3-n0","x":x(1)+470,"y":900,"w":W,"page":"v3","text":"0b 是 app 之外的选项，不是 app 的一屏。今天就能做，因为 /answer 和 Telegram 群都在。它够用，app 就不做。"},
    {"id":"v3-n6","x":x(0),"y":R2+900,"w":W,"page":"v3","text":"三种行：绿「你在回」（已回，等客户）· 灰「佳佳 在回 · 还没回」（别人认领了，清队列会跳过）· 浅绿底 ⚡（没人认领）。收款和 IG/FB 号码是两条入口行，不混进 SOS。"},
    {"id":"v3-n9","x":x(4),"y":R2+900,"w":W,"page":"v3","text":"收款这一屏的规矩来自 bot 自己：bot 永远不确认收款，只有人能。确认 = 现有 /verify，拒绝 = /reject；确认后 bot 接着发报名表，不用人再回。收款账号只认 JWC 官方，非官方会被拦。"},
    {"id":"v3-n11","x":x(2),"y":R3+900,"w":W,"page":"v3","text":"登录只在两种情况出现：第一次装、或 30 天到期。平时都是从通知的签名链接直接进会话。"},
]
canvas = {
  "pages": [{"id":"v3","name":"v3 · 并入九条盲点"}, {"id":"v2","name":"v2 · 存档"}, {"id":"v1","name":"v1 · 存档"}],
  "artboards": v3_boards + v2_boards + v1_boards,
  "annotations": v3_notes + old_notes,
  "launch": {"view":"canvas","page":"v3"},
}
(OUT/'canvas.json').write_text(json.dumps(canvas, ensure_ascii=False, indent=2))
print(len(canvas['artboards']), 'artboards;', len(canvas['annotations']), 'notes')
for f in sorted(OUT.glob('*.dc.html')): print(' ', f.name, f.stat().st_size)
