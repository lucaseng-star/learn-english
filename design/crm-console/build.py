# -*- coding: utf-8 -*-
"""CRM 全链路控制台 —— 6 个画板的唯一来源。
改设计改这里，然后 python3 build.py 重新生成 *.dc.html。
不要直接编辑生成出来的 .dc.html，会被覆盖。
数值一律来自 ../../assets/ui-kit.css 的 token。"""
import re, os

T = dict(
    ink="#14181d", ink2="#3c444e", muted="#7b838e", time="#9aa1ab",
    line="#e9eaec", soft="#f0f1f3", surf="#ffffff", surf2="#f5f6f7", canvas="#fbfbfc",
    brand="#2ec06a", brandsoft="#edf7f0", accent="#dcf8c6", warm="#f4f0e9",
    blue_bg="#e9effd", blue_fg="#3757c8", yel_bg="#fdf3c9", yel_fg="#7a5f18",
    grn_bg="#e6f6ec", grn_fg="#1e7a45", gry_bg="#eef0f2", gry_fg="#545c66",
    ser1="#1e9e55", ser2="#3757c8", bad="#b42318", warn="#c9911c", tick="#4fa8ec",
)

HEAD = '''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <style>
    *, *::before, *::after { box-sizing: border-box; }
    body { margin: 0; font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Arial, sans-serif; -webkit-font-smoothing: antialiased; }
    a { color: #1a73e8; text-decoration: none; }
    a:hover { color: #1557b0; text-decoration: underline; }
    .ic { fill: none; stroke: currentColor; stroke-width: 1.7; stroke-linecap: round; stroke-linejoin: round; }
  </style>
</helmet>

<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><!--ICONS--></defs></svg>
'''

TAIL = '''</x-dc>
<script data-dc-script data-props='{"$preview":{"width":1440,"height":900}}'>
class Component extends DCLogic {}
</script>
</body>
</html>
'''

NAV = [("i-chart","总览"), ("i-chat","工作台"), ("i-contacts","客户"),
       ("i-tag","线索"), ("i-nodes","商机"), ("i-megaphone","营销"), ("i-bag","订单")]

def ic(name, size=20, extra=""):
    return '<svg viewBox="0 0 24 24" width="%d" height="%d" class="ic"%s><use href="#%s"></use></svg>' % (
        size, size, (' style="%s"' % extra) if extra else "", name)

def rail(active):
    btns = []
    for i, (icon, _label) in enumerate(NAV):
        on = (i == active)
        st = ("width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;"
              + ("background:%s;color:#ffffff" % T['brand'] if on else "color:%s" % T['time']))
        btns.append('        <div style="%s">%s</div>' % (st, ic(icon, 21)))
    gear_on = (active == 7)
    gear = ("width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;"
            + ("background:%s;color:#ffffff" % T['brand'] if gear_on else "color:%s" % T['time']))
    return '''    <nav style="display:flex;flex-direction:column;align-items:center;padding:14px 0 22px;background:%s">
      <div style="width:36px;height:36px;display:flex;align-items:center;justify-content:center;color:#ffffff;margin-bottom:26px">%s</div>
      <div style="display:flex;flex-direction:column;gap:10px">
%s
      </div>
      <div style="margin-top:auto;%s">%s</div>
    </nav>''' % (T['ink'], ic("i-bot", 24, "stroke-width:1.9"), "\n".join(btns), gear, ic("i-gear", 21))

def shell(cols, inner):
    return '''
<div style="width:1440px;height:900px;padding:24px;background:%s">
  <div style="display:grid;grid-template-columns:%s;width:1392px;height:852px;background:%s;border-radius:22px;box-shadow:0 1px 2px rgba(16,24,40,.05), 0 24px 60px rgba(16,24,40,.13);overflow:hidden">

%s

  </div>
</div>
''' % (T['canvas'], cols, T['surf'], inner)

def tag(text, kind="gray", size=11.5):  # .uk-tag--sm
    bg, fg = {"gray":(T['gry_bg'],T['gry_fg']), "green":(T['grn_bg'],T['grn_fg']),
              "blue":(T['blue_bg'],T['blue_fg']), "yellow":(T['yel_bg'],T['yel_fg'])}[kind]
    return ('<span style="padding:3px 9px;border-radius:7px;background:%s;color:%s;'
            'font-size:%spx;font-weight:500;white-space:nowrap">%s</span>' % (bg, fg, size, text))

def kpi(label, value, sub, sub_kind="muted"):
    col = {"muted":T['time'], "good":T['grn_fg'], "bad":T['bad']}[sub_kind]
    weight = "600" if sub_kind != "muted" else "400"
    return '''        <div style="padding:16px 18px;border:1px solid %s;border-radius:14px;display:flex;flex-direction:column;gap:6px">
          <span style="font-size:12.5px;color:%s">%s</span>
          <span style="font-size:24px;font-weight:700;letter-spacing:-.02em;color:%s;line-height:1.1">%s</span>
          <span style="font-size:11.5px;font-weight:%s;color:%s">%s</span>
        </div>''' % (T['line'], T['muted'], label, T['ink'], value, weight, col, sub)

def panel_head(title, right="", sub=""):
    subhtml = ('<p style="margin:1px 0 0;font-size:12.5px;color:%s">%s</p>' % (T['muted'], sub)) if sub else ""
    return '''      <div style="display:flex;align-items:center;gap:8px;padding:23px 18px 12px">
        <div style="min-width:0"><h1 style="margin:0;font-size:20px;font-weight:700;letter-spacing:-.01em;color:%s">%s</h1>%s</div>
        <div style="margin-left:auto;display:flex;gap:2px;color:%s">%s</div>
      </div>''' % (T['ink'], title, subhtml, T['gry_fg'], right)

def aside_head(title, sub=""):
    subhtml = ('<p style="margin:4px 0 0;font-size:12.5px;color:%s">%s</p>' % (T['muted'], sub)) if sub else ""
    return '''      <div style="padding:31px 18px 27px;border-bottom:1px solid %s">
        <h2 style="margin:0;font-size:16px;font-weight:700;letter-spacing:-.01em;color:%s">%s</h2>%s
      </div>''' % (T['line'], T['ink'], title, subhtml)

def btn_primary(label, icon=None):
    g = (ic(icon, 15, "stroke-width:2.2") + " ") if icon else ""
    return ('<span style="display:flex;align-items:center;justify-content:center;gap:6px;height:34px;padding:0 14px;'
            'border-radius:10px;background:%s;color:#ffffff;font-size:13.5px;font-weight:600;white-space:nowrap">%s%s</span>' % (T['brand'], g, label))

def btn_ghost(label, icon=None):
    g = (ic(icon, 16) + " ") if icon else ""
    return ('<span style="display:flex;align-items:center;justify-content:center;gap:6px;height:34px;padding:0 14px;'
            'border:1px solid %s;border-radius:10px;font-size:13.5px;font-weight:500;color:%s;white-space:nowrap">%s%s</span>' % (T['line'], T['ink2'], g, label))

def icon_btn(name):
    return ('<span style="width:32px;height:32px;display:flex;align-items:center;justify-content:center;border-radius:7px">%s</span>' % ic(name))

def write(name, cols, inner):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), name + ".dc.html")
    open(path, "w", encoding="utf-8").write(HEAD + shell(cols, inner) + TAIL)
    return path

def inject_icons():
    src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../assets/ui-icons.svg"), encoding="utf-8").read()
    here = os.path.dirname(os.path.abspath(__file__))
    want = ['i-chart','i-chat','i-contacts','i-tag','i-nodes','i-megaphone','i-bag','i-gear',
            'i-search','i-filter','i-more','i-chevron','i-plus','i-check2','i-user','i-info',
            'i-quick','i-play','i-clip','i-emoji','i-mic','i-verified','i-phone','i-bot','i-team']
    defs = "\n".join(re.search(r'<symbol id="%s".*?</symbol>' % w, src, re.S).group(0) for w in want)
    for f in sorted(os.listdir(here)):
        if not f.endswith(".dc.html"): continue
        p = os.path.join(here, f)
        t = open(p, encoding="utf-8").read()
        t = t.replace("<!--ICONS-->", "\n" + defs + "\n")
        open(p, "w", encoding="utf-8").write(t)
        used = set(re.findall(r'href="#(i-[a-z0-9-]+)"', t))
        miss = used - set(want)
        assert not miss, (f, miss)
    print("图标注入完成，未定义引用：0")


# ══ 构建期检查：不合规的数值直接让构建失败 ═══════════════
FS_OK   = {"10.5","11.5","12.5","13.5","14","16","20","24"}
RAD_OK  = {"2","7","10","12","14","22","999","50%"}
HEX_OK  = {v.lower() for v in T.values()} | {"#ffffff","#fff","#f4f5f6","#a3aab3"}

def lint():
    here = os.path.dirname(os.path.abspath(__file__))
    bad = []
    for f in sorted(os.listdir(here)):
        if not f.endswith(".dc.html"): continue
        t = open(os.path.join(here, f), encoding="utf-8").read()
        body = t.split("</helmet>", 1)[1]                 # helmet 里的重置样式不参与
        body = re.sub(r'<svg width="0".*?</svg>', "", body, flags=re.S)   # 图标 sprite 不参与
        for m in re.finditer(r'font-size:\s*([\d.]+)px', body):
            if m.group(1) not in FS_OK: bad.append((f, "字号", m.group(1) + "px"))
        for m in re.finditer(r'border-radius:\s*([^;"]+)', body):
            for v in m.group(1).replace("%", "% ").split():
                v = v.replace("px", "").strip()
                if v and v not in RAD_OK: bad.append((f, "圆角", v))
        for m in re.finditer(r'#[0-9a-fA-F]{3,6}', body):
            if m.group(0).lower() not in HEX_OK: bad.append((f, "颜色", m.group(0)))
    if bad:
        seen, lines = set(), []
        for row in bad:
            if row in seen: continue
            seen.add(row); lines.append("  %s  %s  %s" % row)
        raise SystemExit("设计 token 检查未通过（%d 处）：\n%s" % (len(lines), "\n".join(lines)))
    print("token 检查通过：字号/圆角/颜色全部来自 ui-kit.css")
