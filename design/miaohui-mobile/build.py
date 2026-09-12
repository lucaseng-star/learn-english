# 生成「秒回」手机端设计稿的 .dc.html 画板 —— 内容全部取自 jwc-bot 真实模式，视觉取自 ui-kit token
import json, pathlib
OUT = pathlib.Path(__file__).resolve().parent; OUT.mkdir(parents=True, exist_ok=True)

# ── ui-kit tokens（精确值，来自 assets/ui-kit.css）──
INK='#14181d'; INK2='#3c444e'; MUTED='#7b838e'; TIME='#9aa1ab'; LINE='#e9eaec'; LINE_SOFT='#f0f1f3'
SURF='#ffffff'; SURF2='#f5f6f7'; CANVAS='#fbfbfc'; BRAND='#2ec06a'; BRAND_SOFT='#edf7f0'; ACCENT='#dcf8c6'
WARM='#f4f0e9'; LINK='#1a73e8'; TICK='#4fa8ec'
TAG = {'blue':('#e9effd','#3757c8'), 'yellow':('#fdf3c9','#7a5f18'), 'green':('#e6f6ec','#1e7a45'), 'gray':('#eef0f2','#545c66')}
WAIT = {'hot':('#fdecea','#c0392b'), 'warm':('#fdf3c9','#8a6410'), 'cool':('#e6f6ec','#1e7a45')}
STAGE = {'hot':('#dc2626','热'), 'considering':('#f0c040','考虑中'), 'curious':('#7fc6ff','好奇'), 'cold':('#6a6f7a','冷'), 'enrolled':('#16a34a','已报名')}  # dashboard 同色

ICONS = {
 'search':'<circle cx="11" cy="11" r="6.4"/><path d="m20 20-4.4-4.4"/>',
 'gear':'<path d="M19.5 15.2a1.7 1.7 0 0 0 .34 1.87l.06.06a2.05 2.05 0 1 1-2.9 2.9l-.06-.06a1.7 1.7 0 0 0-1.87-.34 1.7 1.7 0 0 0-1.03 1.55v.17a2.05 2.05 0 0 1-4.1 0v-.09a1.7 1.7 0 0 0-1.11-1.55 1.7 1.7 0 0 0-1.87.34l-.06.06a2.05 2.05 0 1 1-2.9-2.9l.06-.06a1.7 1.7 0 0 0 .34-1.87 1.7 1.7 0 0 0-1.55-1.03H2.6a2.05 2.05 0 0 1 0-4.1h.09A1.7 1.7 0 0 0 4.24 8.8a1.7 1.7 0 0 0-.34-1.87l-.06-.06a2.05 2.05 0 1 1 2.9-2.9l.06.06a1.7 1.7 0 0 0 1.87.34h.08A1.7 1.7 0 0 0 9.78 2.8v-.17a2.05 2.05 0 0 1 4.1 0v.09a1.7 1.7 0 0 0 1.03 1.55 1.7 1.7 0 0 0 1.87-.34l.06-.06a2.05 2.05 0 1 1 2.9 2.9l-.06.06a1.7 1.7 0 0 0-.34 1.87v.08a1.7 1.7 0 0 0 1.55 1.03h.17a2.05 2.05 0 0 1 0 4.1h-.09a1.7 1.7 0 0 0-1.55 1.03Z"/><circle cx="12" cy="12" r="3"/>',
 'chevron':'<path d="m9.5 5.6 6.4 6.4-6.4 6.4"/>',
 'more':'<circle cx="12" cy="5.4" r="1.5" fill="currentColor" stroke="none"/><circle cx="12" cy="12" r="1.5" fill="currentColor" stroke="none"/><circle cx="12" cy="18.6" r="1.5" fill="currentColor" stroke="none"/>',
 'mic':'<rect x="9.2" y="3.2" width="5.6" height="10.4" rx="2.8"/><path d="M5.8 11.4a6.2 6.2 0 0 0 12.4 0M12 17.6v3.2"/>',
 'check2':'<path d="m1.6 12.6 3.9 4 6.7-8"/><path d="m8.4 12.9 3.3 3.4 8.7-9.9"/>',
 'info':'<circle cx="12" cy="12" r="8.6"/><path d="M12 11.2v4.6"/><circle cx="12" cy="8.2" r=".95" fill="currentColor" stroke="none"/>',
 'play':'<path fill="currentColor" stroke="none" d="M8.4 5.6 18.6 12 8.4 18.4Z"/>',
 'bolt':'<path d="M13.4 2.6 5.2 13.4h5.1l-.9 8 8.4-11h-5.2Z"/>',
 'clock':'<circle cx="12" cy="12" r="8.6"/><path d="M12 7.2V12l3.4 2.1"/>',
 'send':'<path d="M20.6 3.4 3.6 10.2l6.5 2.6M20.6 3.4l-3 17-4.1-5.9M20.6 3.4 10.1 12.8v5.5l3.4-3.4"/>',
 'asterisk':'<path fill="currentColor" stroke="none" d="M12 2.4c.9 0 1.6.7 1.6 1.6v4.5l3.2-3.2a1.6 1.6 0 1 1 2.3 2.3l-3.2 3.2H20a1.6 1.6 0 1 1 0 3.2h-4.1l3.2 3.2a1.6 1.6 0 1 1-2.3 2.3l-3.2-3.2V20a1.6 1.6 0 1 1-3.2 0v-4.1l-3.2 3.2a1.6 1.6 0 0 1-2.3-2.3l3.2-3.2H4a1.6 1.6 0 1 1 0-3.2h4.1L4.9 7.6a1.6 1.6 0 0 1 2.3-2.3l3.2 3.2V4c0-.9.7-1.6 1.6-1.6Z"/>',
 'tag':'<path d="M7.9 10.4V8.2a4.1 4.1 0 0 1 8.2 0v2.2"/><rect x="4.6" y="10.4" width="14.8" height="9.6" rx="3.2"/>',
 'note':'<path d="M13.8 3.4H7.4a2 2 0 0 0-2 2v13.2a2 2 0 0 0 2 2h9.2a2 2 0 0 0 2-2V8.2Z"/><path d="M13.6 3.6v4.4h4.6M8.8 13h6.4M8.8 16.4h4.2"/>',
 'phone':'<path d="M6.3 3.8h2.1l1.7 4.1-2 1.4a11.4 11.4 0 0 0 5.2 5.2l1.4-2 4.1 1.7v2.1a2.4 2.4 0 0 1-2.6 2.4A14.3 14.3 0 0 1 3.9 6.4a2.4 2.4 0 0 1 2.4-2.6Z"/>',
 'image':'<rect x="3.6" y="5.2" width="16.8" height="13.6" rx="2.2"/><circle cx="8.6" cy="9.6" r="1.6"/><path d="m20.4 15.2-4.6-4.4-7.2 7.4"/>',
 'folder':'<path d="M3.6 7.2a2 2 0 0 1 2-2h4.2l2 2.2h6.6a2 2 0 0 1 2 2v8.2a2 2 0 0 1-2 2H5.6a2 2 0 0 1-2-2Z"/>',
 'pin':'<path d="M12 21.2s6.4-6 6.4-10.8a6.4 6.4 0 0 0-12.8 0C5.6 15.2 12 21.2 12 21.2Z"/><circle cx="12" cy="10.2" r="2.4"/>',
 'plus':'<path d="M12 5.4v13.2M5.4 12h13.2"/>',
 'clip':'<path d="M18.6 11.4 12 18a4.1 4.1 0 0 1-5.8-5.8l7-7a2.7 2.7 0 0 1 3.9 3.9l-7 7a1.4 1.4 0 0 1-2-2l6.4-6.4"/>',
 'wa':'<path fill="currentColor" stroke="none" d="M12 2.6a9.3 9.3 0 0 0-8 14.1L2.7 21.4l4.9-1.3A9.3 9.3 0 1 0 12 2.6Zm5.2 13c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-1.7-.1a13 13 0 0 1-5.7-4.9c-.4-.6-.9-1.5-.9-2.4 0-.9.5-1.4.7-1.6.2-.2.4-.3.6-.3h.5c.2 0 .4-.1.6.4l.8 1.9c.1.2.1.3 0 .5l-.4.5c-.1.2-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.1 1 2 1.3 2.3 1.4.3.1.4.1.6-.1l.8-1c.2-.2.3-.2.6-.1l1.8.9c.3.1.4.2.5.3.1.2.1.5-.1 1.1Z"/>',
}
def ic(name, size=20, style='', sw=None):
    s = f'flex:none;{style}' + (f'stroke-width:{sw};' if sw else '')
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" class="ic" style="{s}">{ICONS[name]}</svg>'

HEAD = '''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;display=swap">
  <style>
    body { margin: 0; background: #fbfbfc; font-family: Inter, -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Noto Sans SC", "Segoe UI", sans-serif; color: #14181d; -webkit-font-smoothing: antialiased; }
    a { color: #1a73e8; text-decoration: none; } a:hover { color: #1557b0; text-decoration: underline; }
    .ic { fill: none; stroke: currentColor; stroke-width: 1.7; stroke-linecap: round; stroke-linejoin: round; }
    .num { font-variant-numeric: tabular-nums; }
  </style>
</helmet>
'''
TAIL = '''
</x-dc>
</body>
</html>
'''
def phone(inner, bg=SURF):
    return HEAD + f'<div style="width:390px;height:844px;background:{bg};display:flex;flex-direction:column;overflow:hidden;position:relative;font-size:15px;line-height:1.45">\n{inner}\n</div>' + TAIL

# ── 小组件 ──
def iconbtn(name, size=20, w=44, color=INK2):
    return f'<div style="width:{w}px;height:{w}px;display:flex;align-items:center;justify-content:center;border-radius:10px;color:{color}">{ic(name,size)}</div>'
def tag(text, kind='gray', extra=''):
    bg,fg = TAG[kind]
    return f'<span style="padding:3px 8px;border-radius:7px;background:{bg};color:{fg};font-size:11.5px;font-weight:600;white-space:nowrap;{extra}">{text}</span>'
def stage_tag(key):
    col,label = STAGE[key]
    return f'<span style="display:inline-flex;align-items:center;gap:5px;padding:3px 8px;border-radius:7px;background:#eef0f2;color:#545c66;font-size:11.5px;font-weight:600;white-space:nowrap"><span style="width:7px;height:7px;border-radius:50%;background:{col}"></span>{label}</span>'
def wait_pill(text, level):
    bg,fg = WAIT[level]
    return f'<span class="num" style="flex:none;padding:2px 7px;border-radius:7px;background:{bg};color:{fg};font-size:11.5px;font-weight:700">{text}</span>'
def avatar(initial, line_emoji, size=42):
    fs = 15 if size >= 40 else 13
    return (f'<div style="position:relative;width:{size}px;height:{size}px;flex:none">'
            f'<div style="width:{size}px;height:{size}px;border-radius:50%;background:#eef0f2;color:#545c66;display:flex;align-items:center;justify-content:center;font-size:{fs}px;font-weight:700">{initial}</div>'
            f'<div style="position:absolute;right:-3px;bottom:-3px;width:19px;height:19px;border-radius:50%;background:#ffffff;border:1.5px solid #e9eaec;display:flex;align-items:center;justify-content:center;font-size:10px;line-height:1">{line_emoji}</div></div>')
def chip(text, selected=False, count=None):
    c = f' <b class="num" style="font-weight:700;color:{BRAND if selected else TIME}">{count}</b>' if count is not None else ''
    if selected:
        return f'<div style="flex:none;height:34px;padding:0 14px;display:flex;align-items:center;gap:5px;border-radius:999px;background:{INK};color:#ffffff;font-size:13.5px;font-weight:600">{text}{c}</div>'
    return f'<div style="flex:none;height:34px;padding:0 14px;display:flex;align-items:center;gap:5px;border-radius:999px;border:1px solid {LINE};background:{SURF};color:{MUTED};font-size:13.5px;font-weight:600">{text}{c}</div>'
def section(title, count, note=''):
    n = f'<span style="margin-left:auto;font-size:12.5px;color:{TIME}">{note}</span>' if note else ''
    return (f'<div style="display:flex;align-items:center;gap:8px;padding:12px 16px 6px;border-top:1px solid {LINE_SOFT}">'
            f'<span style="font-size:12.5px;font-weight:700;color:{INK2};letter-spacing:.02em">{title}</span>'
            f'<span class="num" style="font-size:12.5px;font-weight:700;color:{BRAND}">{count}</span>{n}</div>')
def primary(label, sub=''):
    s = f'<span class="num" style="opacity:.85;font-weight:600">{sub}</span>' if sub else ''
    return f'<div style="display:flex;align-items:center;justify-content:center;gap:8px;min-height:50px;border-radius:10px;background:{BRAND};color:#ffffff;font-size:15px;font-weight:700">{ic("bolt",16,"stroke-width:2;")}<span>{label}</span>{s}</div>'
def dock(inner):
    return f'<div style="margin-top:auto;padding:12px 16px 20px;border-top:1px solid {LINE};background:{SURF}">{inner}</div>'

# ══════════════════════════ 1. Main —— 待回队列 ══════════════════════════
def sos_row(initial, emoji, name, wait, level, question, tags_html, unread=True):
    bg = BRAND_SOFT if unread else SURF
    return (f'<div style="display:grid;grid-template-columns:42px minmax(0,1fr) 44px;gap:11px;align-items:start;padding:13px 12px 13px 16px;border-bottom:1px solid {LINE_SOFT};background:{bg}">'
            f'{avatar(initial, emoji)}'
            f'<div style="min-width:0;display:flex;flex-direction:column;gap:3px">'
            f'<div style="display:flex;align-items:baseline;gap:8px"><span style="flex:1;min-width:0;font-size:15px;font-weight:600;letter-spacing:-.01em;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{name}</span>{wait_pill(wait, level)}</div>'
            f'<p style="margin:0;font-size:13.5px;line-height:1.38;color:{MUTED};display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden">{question}</p>'
            f'<div style="display:flex;flex-wrap:wrap;gap:5px;margin-top:4px">{tags_html}</div></div>'
            f'<div style="align-self:center;width:44px;height:44px;display:flex;align-items:center;justify-content:center;border-radius:10px;background:{SURF2};color:{INK}">{ic("bolt",19)}</div></div>')

main_inner = f'''
<div style="display:flex;align-items:center;gap:8px;padding:16px 8px 6px 16px">
  <h1 style="margin:0;font-size:21px;font-weight:700;letter-spacing:-.015em">待回</h1>
  <span style="flex:1"></span>
  {iconbtn('search')}{iconbtn('gear')}
</div>
<div style="display:flex;gap:8px;padding:2px 16px 10px;overflow:hidden">
  {chip('全部线', True, 8)}{chip('🍷 Emily', False, 1)}{chip('☕ Cindy', False, 1)}{chip('☕ Coco', False, 1)}{chip('🏢 主号', False, 5)}
</div>
<dl style="display:flex;gap:1px;margin:0 16px 10px;border-radius:10px;background:{SURF2};overflow:hidden">
  <div style="flex:1;padding:9px 10px 10px"><dt style="font-size:11.5px;font-weight:600;color:{MUTED};letter-spacing:.04em">待回</dt><dd class="num" style="margin:1px 0 0;font-size:17px;font-weight:700;letter-spacing:-.02em">8 <span style="font-size:11.5px;font-weight:600;color:#7b838e">= 3 SOS + 5 主号</span></dd></div>
  <div style="flex:1;padding:9px 10px 10px"><dt style="font-size:11.5px;font-weight:600;color:{MUTED};letter-spacing:.04em">最久等</dt><dd class="num" style="margin:1px 0 0;font-size:17px;font-weight:700;letter-spacing:-.02em;color:#c0392b">14 <span style="font-size:12.5px;font-weight:600;color:{MUTED}">分</span></dd></div>
  <div style="flex:1;padding:9px 10px 10px"><dt style="font-size:11.5px;font-weight:600;color:{MUTED};letter-spacing:.04em">今日回了</dt><dd class="num" style="margin:1px 0 0;font-size:17px;font-weight:700;letter-spacing:-.02em">11</dd></div>
</dl>
<div style="flex:1;min-height:0;overflow:hidden;display:flex;flex-direction:column">
  {section('🆘 等真人', 3, 'Bot 已承诺「5-10 分钟真人回你」')}
  {sos_row('S','🍷','Sharon','等 14 分','hot','刚毕业。如果中途找到全职工作可以转周末班吗？学费怎么算？', tag('WNSM 调酒半工读','blue')+stage_tag('hot')+tag('Meta 广告','gray'))}
  {sos_row('W','☕','Wei Jie','等 7 分','warm','BMART diploma 是不是 PTPK 可以全额？我 SPM 只有 3 credit 够吗', tag('BMART Diploma','blue')+stage_tag('considering')+tag('FB 广告','gray'))}
  {sos_row('A','☕','Aina','等 3 分','cool','Boleh dapat sijil untuk kelas Barista 1 hari tak? Nak guna untuk apply kerja', tag('1-Day Junior Barista (BM/EN)','blue')+stage_tag('curious')+tag('IG 帖子','gray'))}
  {section('📞 IG/FB 给了号码', 2, '等你打 WhatsApp')}
  <div style="display:grid;grid-template-columns:36px minmax(0,1fr) auto;gap:10px;align-items:center;padding:10px 16px;border-bottom:1px solid {LINE_SOFT}">
    {avatar('N','☕',36)}
    <div style="min-width:0"><div style="font-size:14px;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">Nurul <span style="font-weight:500;color:{MUTED}">@nurul.bakes · JWC Bakery (IG)</span></div>
    <div style="font-size:12.5px;color:{MUTED};overflow:hidden;text-overflow:ellipsis;white-space:nowrap">my number 012-345 6789, boleh call petang · <span class="num">18 分钟前</span></div></div>
    <div style="height:34px;padding:0 12px;display:flex;align-items:center;gap:6px;border-radius:999px;background:{SURF2};font-size:13px;font-weight:600;color:{INK}">{ic('wa',15)}打开</div>
  </div>
  <div style="padding:8px 16px 4px;font-size:12.5px;color:{LINK}">还有 1 条 ›</div>
</div>
{dock(primary('开始清队列', '· 3 条'))}
'''
(OUT/'Main.dc.html').write_text(phone(main_inner))

# ══════════════════════════ 会话相关共用 ══════════════════════════
def chat_head(name, sub):
    return (f'<div style="display:flex;align-items:center;gap:8px;padding:10px 8px 10px 4px;border-bottom:1px solid {LINE};background:{SURF}">'
            f'<div style="width:44px;height:44px;display:flex;align-items:center;justify-content:center;color:{INK}">{ic("chevron",24,"transform:scaleX(-1);")}</div>'
            f'{avatar(name[0], "🍷")}'
            f'<div style="flex:1;min-width:0"><div style="font-size:17px;font-weight:700;letter-spacing:-.015em;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{name}</div><div style="font-size:12.5px;color:{MUTED}">{sub}</div></div>'
            f'{iconbtn("more")}</div>')
def takeover_bar(taken=False, compact=False):
    if compact:
        return (f'<div style="display:flex;align-items:center;gap:8px;padding:8px 16px;background:{BRAND_SOFT};border-bottom:1px solid {LINE};font-size:12.5px;font-weight:600;color:#1e7a45">'
                f'<span>🟢 人手中 · Boon</span><span style="font-weight:500;color:#3c7a55">· 12 小时没动静自动放回 Bot</span></div>')
    if not taken:
        return (f'<div style="display:flex;align-items:center;gap:10px;padding:9px 12px 9px 16px;background:#fdf3c9;border-bottom:1px solid {LINE}">'
                f'<div style="flex:1;min-width:0;font-size:13px;font-weight:600;color:#7a5f18;line-height:1.35">Bot 还在回这个对话<br><span style="font-weight:500">WhatsApp 线：你回一句，bot 会继续跟。先停它再回。</span></div>'
                f'<div style="flex:none;height:38px;padding:0 13px;display:flex;align-items:center;border-radius:10px;background:{INK};color:#ffffff;font-size:13.5px;font-weight:700;white-space:nowrap">🔴 我接管 / 停 bot</div></div>')
    return (f'<div style="display:flex;align-items:center;gap:10px;padding:9px 12px 9px 16px;background:{BRAND_SOFT};border-bottom:1px solid {LINE}">'
            f'<div style="flex:1;min-width:0;font-size:13px;font-weight:600;color:#1e7a45;line-height:1.35">人手中 · Boon<br><span style="font-weight:500">Bot 已停。12 小时没动静会自动放回 Bot。</span></div>'
            f'<div style="flex:none;height:38px;padding:0 13px;display:flex;align-items:center;border-radius:10px;border:1px solid {LINE};background:{SURF};color:{INK};font-size:13.5px;font-weight:700;white-space:nowrap">🟢 让 Bot 接管</div></div>')
def ctx_strip(open_=False):
    head = (f'<div style="display:flex;align-items:center;gap:7px;padding:10px 16px;font-size:13.5px;font-weight:600;color:{INK2}">{ic("info",16,"color:#7b838e;","2")}'
            f'<span style="flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">Meta 广告 · WNSM 调酒半工读 · 热</span>{ic("chevron",16,"color:#7b838e;transform:rotate(90deg);" if open_ else "color:#7b838e;","2")}</div>')
    if not open_:
        return f'<div style="border-bottom:1px solid {LINE};background:{SURF}">{head}</div>'
    def cell(k, v, wide=False):
        return f'<div style="{"grid-column:1 / -1;" if wide else ""}min-width:0;padding:4px 0"><dt style="font-size:11.5px;font-weight:600;color:{MUTED};letter-spacing:.03em">{k}</dt><dd style="margin:1px 0 0;font-size:13.5px;font-weight:600">{v}</dd></div>'
    grid = ('<dl style="display:grid;grid-template-columns:repeat(2, minmax(0, 1fr));gap:1px 12px;margin:0;padding:0 16px 10px">'
            + cell('来源', 'Meta 广告 · WNSM 半工读 A2', True)
            + cell('咨询课程', 'WNSM 调酒半工读 · 9 个月')
            + cell('阶段', '热 · 问了报名')
            + cell('语言', '中文')
            + cell('资格', '酒精 OK（非 BM 渠道）')
            + cell('Bot 下一步', '唤醒模板 · 明早 9:00')
            + cell('对话', '2 轮 · 首次 今天 11:02')
            + '</dl>')
    return f'<div style="border-bottom:1px solid {LINE};background:{SURF}">{head}{grid}</div>'

def bubble_in(text, t):
    return (f'<div style="display:flex;justify-content:flex-start"><div style="position:relative;max-width:82%;padding:8px 11px 7px;border-radius:9px;border-top-left-radius:2px;background:{SURF};box-shadow:0 1px 1px rgba(16,24,40,.09);font-size:15px;line-height:1.42">'
            f'<p style="margin:0;padding-right:46px;white-space:pre-wrap">{text}</p><span class="num" style="position:absolute;right:9px;bottom:5px;font-size:10.5px;color:{TIME}">{t}</span></div></div>')
def bubble_out(text, t, by, state='read'):
    by_html = f'<span style="display:block;margin:0 0 3px;font-size:11.5px;font-weight:700;color:{BRAND}">{by}</span>'
    if state == 'read':
        meta = f'<span class="num" style="position:absolute;right:9px;bottom:5px;display:flex;align-items:center;gap:3px;font-size:10.5px;color:{TIME}">{t}{ic("check2",14,"color:#4fa8ec;","2.2")}</span>'
    elif state == 'pending':
        meta = f'<span class="num" style="position:absolute;right:9px;bottom:5px;display:flex;align-items:center;gap:3px;font-size:10.5px;color:{TIME}">发送中 {ic("clock",12,"color:#9aa1ab;","2.2")}</span>'
    else:
        meta = f'<span class="num" style="position:absolute;right:9px;bottom:5px;font-size:10.5px;color:#c0392b;font-weight:700">❌ 未送达</span>'
    return (f'<div style="display:flex;justify-content:flex-end"><div style="position:relative;max-width:82%;padding:8px 11px 7px;border-radius:9px;border-top-right-radius:2px;background:{ACCENT};box-shadow:0 1px 1px rgba(16,24,40,.09);font-size:15px;line-height:1.42">'
            f'{by_html}<p style="margin:0;padding-right:58px;white-space:pre-wrap">{text}</p>{meta}</div></div>')
def sos_marker(t):
    return (f'<div style="display:flex;justify-content:center"><div style="max-width:92%;padding:8px 12px;border-radius:10px;background:#fdecea;color:#c0392b;font-size:12.5px;font-weight:600;line-height:1.4;text-align:center">'
            f'🆘 Emily 答不了 · 已告诉客户「5-10 分钟真人回你」<span class="num" style="font-weight:500;color:#a5443a"> · {t}</span></div></div>')
def daysep(text):
    return f'<div style="display:flex;justify-content:center"><span style="padding:3px 10px;border-radius:7px;background:{SURF};box-shadow:0 1px 1px rgba(16,24,40,.09);font-size:11.5px;font-weight:600;color:{MUTED}">{text}</span></div>'
def stream(children, pad_bottom=12):
    return (f'<div style="flex:1;min-height:0;display:flex;flex-direction:column;gap:12px;padding:14px 12px {pad_bottom}px;overflow:hidden;background:{WARM}">' + ''.join(children) + '</div>')
def act(icon, label):
    return f'<div style="flex:1;min-height:38px;display:flex;align-items:center;justify-content:center;gap:5px;border:1px solid {LINE};border-radius:10px;background:{SURF};color:{INK2};font-size:13.5px;font-weight:600">{ic(icon,17)}{label}</div>'
def composer(text='', placeholder='写回复 · 原文照发，不过审'):
    field = (f'<div style="flex:1;min-width:0;min-height:40px;padding:9px 14px;border-radius:22px;background:{SURF2};font-size:15px;line-height:1.4;color:{INK if text else MUTED}">{text or placeholder}</div>')
    send_bg = BRAND if text else SURF2; send_fg = '#ffffff' if text else MUTED
    return (f'<div style="display:flex;align-items:flex-end;gap:4px;padding:8px 8px 20px;border-top:1px solid {LINE};background:{SURF}">'
            f'<div style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;border-radius:10px;color:{INK2}">{ic("asterisk",20)}</div>{field}'
            f'<div style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;border-radius:10px;color:{INK2}">{ic("mic",20)}</div>'
            f'<div style="width:40px;height:40px;flex:none;display:flex;align-items:center;justify-content:center;border-radius:50%;background:{send_bg};color:{send_fg}">{ic("send",20)}</div></div>')

MSGS = [
    daysep('今天'),
    bubble_in('你好 我看到调酒半工读的广告', '11:02'),
    bubble_out('哈喽 Sharon，我是 Emily 🍷 调酒半工读是 9 个月 36 堂，一周上 1 天课，其余时间在合作酒吧带薪实习。你现在是在工作，还是刚毕业？', '11:02', 'Emily · Bot'),
    bubble_in('刚毕业。如果中途找到全职工作可以转周末班吗？学费怎么算？', '11:04'),
    sos_marker('11:04'),
]

# ══════════════════════════ 2. Chat —— 会话 · 接管 ══════════════════════════
chat_inner = (chat_head('Sharon', '🍷 Emily 线 · 等真人 14 分')
    + takeover_bar(False) + ctx_strip(True) + stream(MSGS) + composer())
(OUT/'Chat.dc.html').write_text(phone(chat_inner))

# ══════════════════════════ 回复台抽屉共用 ══════════════════════════
def drawer(active, body, height=600):
    def dtab(label, on):
        return (f'<div style="position:relative;padding:6px 0 9px;font-size:13.5px;font-weight:700;color:{INK if on else MUTED}">{label}'
                + (f'<span style="position:absolute;left:0;right:0;bottom:-1px;height:2.5px;border-radius:2px 2px 0 0;background:{BRAND}"></span>' if on else '') + '</div>')
    lang = ''.join(f'<div style="min-width:38px;height:28px;padding:0 9px;display:flex;align-items:center;justify-content:center;border-radius:999px;font-size:12.5px;font-weight:700;{"background:#ffffff;color:#14181d;box-shadow:0 1px 1px rgba(16,24,40,.09)" if l=="中" else "color:#7b838e"}">{l}</div>' for l in ['中','EN','BM'])
    return (f'<div style="position:absolute;left:0;right:0;bottom:0;height:{height}px;display:flex;flex-direction:column;border-radius:22px 22px 0 0;background:{SURF};box-shadow:0 -2px 24px rgba(16,24,40,.16)">'
            f'<div style="width:38px;height:4px;margin:8px auto 2px;border-radius:2px;background:{LINE}"></div>'
            f'<div style="display:flex;align-items:center;gap:8px;padding:6px 16px 0"><h3 style="margin:0;font-size:15px;font-weight:700">回复台</h3><span style="flex:1"></span><div style="display:flex;gap:2px;padding:3px;border-radius:999px;background:{SURF2}">{lang}</div></div>'
            f'<div style="display:flex;gap:20px;padding:10px 16px 0;border-bottom:1px solid {LINE}">{dtab("AI 草稿", active=="drafts")}{dtab("快捷话术 · 素材", active=="tmpls")}</div>'
            f'<div style="flex:1;min-height:0;overflow:hidden;padding:12px 16px 16px;display:flex;flex-direction:column;gap:8px">{body}</div></div>')
def scrim():
    return '<div style="position:absolute;inset:0;background:rgba(16,24,40,.34)"></div>'
def hint(text):
    return f'<div style="display:flex;gap:7px;align-items:flex-start;margin:0 0 4px;font-size:12.5px;line-height:1.4;color:{MUTED}">{ic("info",16,"color:#7b838e;margin-top:1px;","2")}<span>{text}</span></div>'
def draft(why, text, n, src='目录 ✓'):
    return (f'<div style="padding:11px 12px;border:1px solid {LINE};border-radius:10px;background:{SURF}">'
            f'<div style="display:flex;align-items:center;gap:6px;margin-bottom:5px"><span style="font-size:11.5px;font-weight:700;color:{BRAND};letter-spacing:.02em">{why}</span>{tag(src,"green")}<span class="num" style="margin-left:auto;font-size:11.5px;color:{TIME}">{n} 字</span></div>'
            f'<p style="margin:0;font-size:13.5px;line-height:1.45;color:{INK2};white-space:pre-wrap">{text}</p></div>')

# ══════════════════════════ 3. Reply —— 回复台 · AI 草稿 ══════════════════════════
drafts_body = (hint('草稿只用 Google Sheet 目录里的事实（价格、日期、地点）。点一条填进输入框，改完再发，AI 不会替你发。')
    + draft('答疑 · 约看课', '可以的 Sharon，半工读转周末班随时可以，学费按剩余堂数折算，不会重复收。\n刚毕业的话建议先来看一堂实操（免费），这周六 2 点有一场，帮你留位？', 70)
    + draft('先问情况', 'Sharon 你好，我是 Boon，Emily 的同事。想先了解一下：你是想边找工作边学，还是先专心学完 9 个月？两种情况我推荐的班不一样。', 62)
    + draft('约通话', '这个问题电话讲 3 分钟更清楚。你现在方便吗？不方便的话晚上 8 点后我打给你。', 40, '无价格'))
reply_inner = (chat_head('Sharon', '🍷 Emily 线 · 人手中 · Boon')
    + takeover_bar(True) + ctx_strip(False) + stream(MSGS[:3]) + composer()
    + scrim() + drawer('drafts', drafts_body, 620))
(OUT/'Reply.dc.html').write_text(phone(reply_inner))

# ══════════════════════════ 4. Quick —— 回复台 · 快捷话术 ══════════════════════════
def folder_chip(text, on=False, count=None):
    c = f' <span class="num" style="color:{BRAND if on else TIME}">{count}</span>' if count is not None else ''
    st = f'background:{INK};color:#ffffff;border:1px solid {INK}' if on else f'background:{SURF};color:{MUTED};border:1px solid {LINE}'
    return f'<div style="flex:none;height:32px;padding:0 12px;display:flex;align-items:center;gap:5px;border-radius:999px;font-size:12.5px;font-weight:600;white-space:nowrap;{st}">{text}{c}</div>'
def tmpl_row(name, uses, extra, pinned=False):
    pin = f'<span style="color:{BRAND}">📌</span> ' if pinned else ''
    return (f'<div style="display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid {LINE_SOFT}">'
            f'<div style="flex:1;min-width:0"><div style="font-size:14px;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{pin}{name}</div><div class="num" style="font-size:12px;color:{MUTED}">用过 {uses} 次 · {extra}</div></div>'
            f'<div style="flex:none;height:32px;padding:0 12px;display:flex;align-items:center;border-radius:999px;background:{SURF2};font-size:13px;font-weight:600;color:{INK}">插入</div></div>')
quick_body = (f'<div style="display:flex;align-items:center;gap:8px;height:38px;padding:0 12px;border-radius:999px;background:{SURF2};color:{MUTED};font-size:13.5px">{ic("search",17,"color:#7b838e;")}搜话术（名字或内容）</div>'
    + f'<div style="display:flex;gap:6px;overflow:hidden;padding:2px 0">{folder_chip("📌 置顶",False,3)}{folder_chip("WNSM KL CN",True,9)}{folder_chip("FMC WEEKEND KL CN",False,7)}{folder_chip("WINE KL CN",False,5)}{folder_chip("我的模版",False,4)}</div>'
    + tmpl_row('WNSM KL CN- PRICE', 132, '1 步 · 1 图', True)
    + tmpl_row('WNSM KL CN- SCHEDULE 2026', 87, '2 步 · 2 图')
    + tmpl_row('WNSM KL CN- INTERN BAR LIST', 41, '1 步')
    + tmpl_row('WNSM KL CN- SWITCH WEEKEND', 18, '1 步')
    + f'<div style="margin-top:6px;font-size:11.5px;font-weight:700;color:{MUTED};letter-spacing:.06em">素材</div>'
    + f'<div style="display:grid;grid-template-columns:repeat(2, minmax(0, 1fr));gap:8px">'
    + ''.join(f'<div style="display:flex;align-items:center;gap:9px;padding:11px 12px;border:1px solid {LINE};border-radius:10px;background:{SURF};font-size:13.5px;font-weight:600">{ic(i,18,"color:#3c444e;")}{l}</div>' for i,l in [('note','✅ 报名 form'),('folder','💳 给账号'),('plus','🤝 54d 社群'),('image','📎 课程图')])
    + '</div>'
    + f'<div style="font-size:11.5px;color:{MUTED};line-height:1.4">💳 只发 JWC 官方账号；非官方收款账号会被拦下并告警。</div>')
quick_inner = (chat_head('Sharon', '🍷 Emily 线 · 人手中 · Boon')
    + takeover_bar(True) + ctx_strip(False) + stream(MSGS[:3]) + composer()
    + scrim() + drawer('tmpls', quick_body, 660))
(OUT/'Quick.dc.html').write_text(phone(quick_inner))

# ══════════════════════════ 5. Sent —— 发完之后 ══════════════════════════
sent_msgs = [MSGS[3], MSGS[4], bubble_out('可以的 Sharon，半工读转周末班随时可以，学费按剩余堂数折算，不会重复收。周六 2 点有一堂免费实操，帮你留位？', '11:19', 'Boon · 人手', 'read')]
def sheet_btn(label, sub='', primary_=False):
    st = f'background:{BRAND};color:#ffffff' if primary_ else f'background:{SURF};color:{INK};border:1px solid {LINE}'
    s = f'<span style="font-size:12px;font-weight:500;opacity:.8">{sub}</span>' if sub else ''
    return f'<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;min-height:50px;border-radius:10px;font-size:14.5px;font-weight:700;{st}">{label}{s}</div>'
sent_sheet = (f'<div style="position:absolute;left:12px;right:12px;bottom:20px;border-radius:14px;background:{SURF};box-shadow:0 -2px 24px rgba(16,24,40,.16);padding:16px 16px 14px;display:flex;flex-direction:column;gap:10px">'
    f'<div style="display:flex;align-items:center;gap:8px"><span style="font-size:15px;font-weight:700">回了 Sharon</span>{tag("✓✓ 已送达","green")}{tag("SOS 已解决","green")}</div>'
    f'<div style="font-size:13px;color:{MUTED};line-height:1.4">Bot 现在停着。不点任何一个，12 小时没动静会自动放回 Bot。</div>'
    + sheet_btn('🟢 让 Bot 接管', '继续自动跟进 · 唤醒模板照排')
    + f'<div style="display:grid;grid-template-columns:repeat(2, minmax(0, 1fr));gap:8px">{sheet_btn("🔴 继续人手","我来跟到底")}{sheet_btn("🕒 稍后跟进","明早 9:00 提醒我")}</div>'
    + f'<div style="display:flex;align-items:center;gap:10px;margin-top:4px;padding-top:12px;border-top:1px solid {LINE_SOFT}">'
    f'<div style="flex:1;min-width:0"><div style="font-size:12px;font-weight:600;color:{MUTED}">队列 <span class="num">1 / 3</span> · 下一条</div><div style="font-size:14px;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">Wei Jie · ☕ Cindy 线 · <span class="num" style="color:#8a6410">等 9 分</span></div></div>'
    f'<div style="flex:none;height:44px;padding:0 16px;display:flex;align-items:center;gap:6px;border-radius:10px;background:{INK};color:#ffffff;font-size:14px;font-weight:700">下一条 {ic("chevron",16,"","2")}</div></div></div>')
sent_inner = (chat_head('Sharon', '🍷 Emily 线 · 人手中 · Boon')
    + takeover_bar(True, compact=True) + stream(sent_msgs) + composer() + scrim() + sent_sheet)
(OUT/'Sent.dc.html').write_text(phone(sent_inner))

# ══════════════════════════ 6. Handoff —— IG/FB 号码交接 ══════════════════════════
def handoff_row(initial, emoji, name, handle, account, course, lang, stage, said, when, waNumber):
    handle_html = f' <span style="font-weight:500;color:{MUTED}">{handle}</span>' if handle else ''
    return (f'<div style="padding:13px 16px;border-bottom:1px solid {LINE_SOFT};display:flex;flex-direction:column;gap:8px">'
            f'<div style="display:grid;grid-template-columns:42px minmax(0,1fr);gap:11px;align-items:center">{avatar(initial,emoji)}'
            f'<div style="min-width:0"><div style="display:flex;align-items:baseline;gap:8px"><span style="flex:1;min-width:0;font-size:15px;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{name}{handle_html}</span><span class="num" style="flex:none;font-size:11.5px;color:{TIME}">{when}</span></div>'
            f'<div style="font-size:12.5px;color:{MUTED};overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{account}</div></div></div>'
            f'<p style="margin:0;padding:8px 11px;border-radius:9px;border-top-left-radius:2px;background:{SURF};box-shadow:0 1px 1px rgba(16,24,40,.09);font-size:13.5px;line-height:1.4;color:{INK}">{said}</p>'
            f'<div style="display:flex;flex-wrap:wrap;gap:5px">{tag(course,"blue")}{stage_tag(stage)}{tag(lang,"gray")}</div>'
            f'<div style="display:grid;grid-template-columns:minmax(0,1fr) auto;gap:8px">'
            f'<div style="min-height:44px;display:flex;align-items:center;justify-content:center;gap:7px;border-radius:10px;background:{BRAND};color:#ffffff;font-size:14px;font-weight:700">{ic("wa",17)}打开 WhatsApp <span class="num" style="font-weight:600;opacity:.85">{waNumber}</span></div>'
            f'<div style="min-height:44px;padding:0 14px;display:flex;align-items:center;justify-content:center;gap:6px;border-radius:10px;border:1px solid {LINE};background:{SURF};font-size:14px;font-weight:600;color:{INK2}">{ic("check2",16,"","2")}已联系</div></div></div>')
handoff_inner = (f'<div style="display:flex;align-items:center;gap:6px;padding:10px 8px 6px 4px">'
    f'<div style="width:44px;height:44px;display:flex;align-items:center;justify-content:center;color:{INK}">{ic("chevron",24,"transform:scaleX(-1);")}</div>'
    f'<h1 style="margin:0;font-size:21px;font-weight:700;letter-spacing:-.015em">IG/FB 给了号码</h1></div>'
    f'<div style="display:flex;gap:20px;padding:0 16px;border-bottom:1px solid {LINE}">'
    f'<div style="position:relative;padding:6px 0 9px;font-size:13.5px;font-weight:700;color:{INK}">待联系 <span class="num" style="color:{BRAND}">2</span><span style="position:absolute;left:0;right:0;bottom:-1px;height:2.5px;border-radius:2px 2px 0 0;background:{BRAND}"></span></div>'
    f'<div style="padding:6px 0 9px;font-size:13.5px;font-weight:700;color:{MUTED}">已联系 <span class="num" style="color:{TIME}">6</span></div></div>'
    + hint('客户在 IG/FB 私信里给了 WhatsApp 号码。IG/FB 那边只有 24 小时回复窗口，转到 WhatsApp 才好继续。点「已联系」名单才会变短。').replace('margin:0 0 4px', 'margin:0;padding:10px 16px 4px')
    + f'<div style="flex:1;min-height:0;overflow:hidden;background:{CANVAS}">'
    + handoff_row('N','☕','Nurul','@nurul.bakes','Instagram · JWC Bakery 账号 · 来自「Sourdough 短片」','BWC Bakery Weekend','BM','considering','my number 012-345 6789, boleh call petang. Nak tanya pasal kelas roti weekend tu','18 分钟前','012-345 6789')
    + handoff_row('K','☕','Kelvin Tan','','Facebook · JWC Academy 专页 · 来自「4 日咖啡速成」广告','FCC 4 日咖啡速成','中文','hot','0176543210 这个是我的 WhatsApp，你 WhatsApp 我，我要问下个月的班','1 小时前','017-654 3210')
    + '</div>')
(OUT/'Handoff.dc.html').write_text(phone(handoff_inner, CANVAS))

# ══════════════════════════ canvas.json ══════════════════════════
W,H,GAP = 390,844,80
xs = [i*(W+GAP) for i in range(6)]
canvas = {
  "artboards": [
    {"file":"Main.dc.html",   "x":xs[0],"y":0,"w":W,"h":H,"title":"1 · 待回队列"},
    {"file":"Chat.dc.html",   "x":xs[1],"y":0,"w":W,"h":H,"title":"2 · 会话 · 接管"},
    {"file":"Reply.dc.html",  "x":xs[2],"y":0,"w":W,"h":H,"title":"3 · 回复台 · AI 草稿"},
    {"file":"Quick.dc.html",  "x":xs[3],"y":0,"w":W,"h":H,"title":"4 · 回复台 · 快捷话术"},
    {"file":"Sent.dc.html",   "x":xs[4],"y":0,"w":W,"h":H,"title":"5 · 发完之后"},
    {"file":"Handoff.dc.html","x":xs[5],"y":0,"w":W,"h":H,"title":"6 · IG/FB 号码交接"},
  ],
  "annotations": [
    {"id":"scope","x":0,"y":-330,"w":640,"text":"范围：只做「回复」这一件事的手机壳，不碰 dashboard 其它功能。\n数据与流程全部取自 jwc-bot：\n· 队列 = /api/escalations/active（SOS 等真人，最久没回的排最上，API 已这样排）\n· 会话 = /conversation/:chatId（含 Bot 下一步 nextHook、9-22 点唤醒时段）\n· 发送 = /api/reply（原文照发不过审、5 秒去重、4000 字、外部收款账号拦截）\n· 话术 = /api/quick-replies（ChatDaddy 导入的资料夹、置顶、用过次数、多步带图）\n· 接管 = /api/takeover 与「🔴 我接管 / 停 bot」「🟢 让 Bot 接管」同一套\n· IG/FB 号码 = /api/igfb-handoffs + contacted\n视觉沿用收件箱复刻的 ui-kit token（Inter、绿 #2ec06a、22px 圆角），不是现有 dashboard 的深色风格；要换一句话。\n人名、消息、价格皆为示例；价格真值只来自 Google Sheet 目录。"},
    {"id":"backend","x":720,"y":-330,"w":600,"text":"你确认设计之前不动任何代码。届时需要后端新增的只有三处：\n① AI 草稿 —— 现在没有。后端按「客户最后一句 + Sheet 目录 + 客户语言」生成 3 条，只准用目录里的事实（同 bot 的白名单闸），前端结构不变。\n② 手机上「认领」—— 现有认领是 email / Telegram 里的签名链接（GET /escalation/claim，先点先得）。app 需要一个带登录态的 POST，语义不变：认领即关闭 open、其他人看到「已被 X 认领」。\n③ 主号（真人线）「谁还没被回」—— 主号 10,756 位客人，/leads 一次 400 行，现在没有「未回」端点。第 1 屏的「🏢 主号 5」要靠它。\n其它全部是现有接口，改的是壳。"},
    {"id":"sla","x":xs[0],"y":900,"w":W,"text":"等待色阶取自 bot 自己的承诺：Emily / Cindy / Coco 在 SOS 时会告诉客户「5-10 分钟真人回你」。\n<5 分绿 · 5-10 分黄 · >10 分红。\n第一行 Sharon 等了 14 分，已经食言。"},
    {"id":"takeover","x":xs[1],"y":900,"w":W,"text":"WhatsApp 线的既有规矩：同事回一句，bot 会继续跟（刻意的）。所以回之前先「🔴 我接管 / 停 bot」，和 dashboard 同一个按钮、同一个含义。\nIG/FB 线：同事一开口 bot 自动让位，这条横幅不出现。\n上下文条只放回复时用得上的：来源、课程、阶段、语言、酒精资格、Bot 下一步。"},
    {"id":"drafts","x":xs[2],"y":900,"w":W,"text":"AI 草稿的每条都带策略标签（答疑 / 先问 / 约通话）和「目录 ✓」—— 表示价格日期来自 Sheet，没有编。\n这是 6/13 RM500 编价事故之后最该有的一道锁。草稿只填进输入框，发送永远是人按。"},
    {"id":"quick","x":xs[3],"y":900,"w":W,"text":"资料夹和名字照 ChatDaddy 导入的原样（WNSM KL CN- PRICE 这种），置顶优先、用过次数排序，和 lib/quick-replies.js 的 list() 一致。\n素材四格对应 dashboard 现有动作：报名 form、给账号、54d 社群、课程图。"},
    {"id":"after","x":xs[4],"y":900,"w":W,"text":"每次回完都要做同一个决定：交还 Bot 还是继续人手。\n暂停有期限：PAUSE_TTL_HOURS=12，12 小时没动静自动放回（PAUSE_AUTO_RESUME=1 才真放回，否则只报名单）。\n清队列模式在这里接「下一条」。"},
    {"id":"handoff","x":xs[5],"y":900,"w":W,"text":"IG/FB 客户给了 WhatsApp 号码，等人打。行内直接「打开 WhatsApp」（wa.me），点「已联系」写 waHandoff.contactedAt，名单才会变短，同事不会打两次。"},
  ],
  "launch": {"view":"canvas"},
}
(OUT/'canvas.json').write_text(json.dumps(canvas, ensure_ascii=False, indent=2))
for f in sorted(OUT.iterdir()): print(f.name, f.stat().st_size)
