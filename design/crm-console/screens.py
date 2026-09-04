# -*- coding: utf-8 -*-
import build as B
from build import T, ic, rail, tag, kpi, panel_head, aside_head, btn_primary, btn_ghost, icon_btn, write

# ══ 1. 闭环总览 ══════════════════════════════════════════
FUNNEL = [
    ("曝光",   "1,240,000", None,   "+6.1%",  "good"),
    ("点击",   "38,400",    3.1,    "+9.4%",  "good"),
    ("进站",   "31,200",    81.3,   "+8.0%",  "good"),
    ("咨询",   "4,180",     13.4,   "+21.3%", "good"),
    ("线索",   "2,340",     56.0,   "+14.6%", "good"),
    ("商机",   "720",       30.8,   "−4.2%",  "bad"),
    ("成交",   "268",       37.2,   "+18.6%", "good"),
]
FG = "150px 130px minmax(0,1fr) 78px 82px"
frows = []
for i, (name, count, rate, delta, kind) in enumerate(FUNNEL):
    bd = "" if i == len(FUNNEL) - 1 else "border-bottom:1px solid %s;" % T['soft']
    if rate is None:
        bar = ('<span style="position:relative;display:block;width:100%%;height:7px;border-radius:999px;background:%s"></span>' % T['gry_bg'])
        rtxt = '<span style="font-size:12.5px;color:%s">基准</span>' % T['time']
    else:
        bar = ('<span style="position:relative;display:block;width:100%%;height:7px;border-radius:999px;background:%s">'
               '<span style="position:absolute;left:0;top:0;width:%s%%;height:7px;border-radius:999px;background:%s"></span></span>'
               % (T['gry_bg'], rate, T['ser1']))
        rtxt = '<span style="font-size:12.5px;font-weight:600;color:%s">%s%%</span>' % (T['ink2'], rate)
    dcol = T['grn_fg'] if kind == "good" else T['bad']
    frows.append('''            <div style="display:grid;grid-template-columns:%s;gap:16px;align-items:center;height:40px;%s">
              <span style="display:flex;align-items:center;gap:9px;font-size:13.5px;font-weight:600;color:%s"><span style="width:20px;height:20px;border-radius:7px;background:%s;color:%s;display:flex;align-items:center;justify-content:center;font-size:10.5px;font-weight:700">%d</span>%s</span>
              <span style="font-size:14px;font-weight:700;letter-spacing:-.01em;color:%s">%s</span>
              %s
              %s
              <span style="justify-self:end;font-size:12.5px;font-weight:600;color:%s">%s</span>
            </div>''' % (FG, bd, T['ink'], T['gry_bg'], T['gry_fg'], i+1, name, T['ink'], count, bar, rtxt, dcol, delta))

CH = [
    ("付费搜索", "HK$92,400", "1,024", "118", "HK$341,200", "HK$90",  "3.69", False),
    ("社媒广告", "HK$61,800",   "712",  "79", "HK$219,400", "HK$87",  "3.55", False),
    ("EDM 邮件", "HK$8,200",    "286",  "41", "HK$118,600", "HK$29", "14.46", False),
    ("自然搜索", "—",           "241",  "22", "HK$48,900",  "—",         "—", False),
    ("KOL 合作", "HK$24,000",    "77",   "8", "HK$14,500",  "HK$312", "0.60", True),
]
CG = "minmax(0,1fr) 104px 84px 84px 128px 104px 76px"
crows = []
for i, (name, spend, leads, deals, rev, cpl, roas, loss) in enumerate(CH):
    bd = "" if i == len(CH) - 1 else "border-bottom:1px solid %s;" % T['soft']
    rcol = T['bad'] if loss else T['ink']
    crows.append('''            <div style="display:grid;grid-template-columns:%s;gap:14px;align-items:center;height:34px;%s">
              <span style="font-size:13.5px;font-weight:600;color:%s">%s</span>
              <span style="font-size:13.5px;color:%s">%s</span>
              <span style="font-size:13.5px;color:%s">%s</span>
              <span style="font-size:13.5px;font-weight:600;color:%s">%s</span>
              <span style="font-size:13.5px;color:%s">%s</span>
              <span style="font-size:13.5px;color:%s">%s</span>
              <span style="justify-self:end;font-size:13.5px;font-weight:700;color:%s">%s</span>
            </div>''' % (CG, bd, T['ink'], name, T['ink2'], spend, T['ink2'], leads,
                         T['ink'], deals, T['ink2'], rev, T['ink2'], cpl, rcol, roas))

todo = [("超时未回会话", "4", "最久 22 分钟未响应", "bad"),
        ("待跟进商机",   "11", "其中 3 个停留超 7 天", "warn"),
        ("未分配线索",   "7", "均来自 KOL 合作", "muted")]
todo_html = []
for i, (name, n, sub, kind) in enumerate(todo):
    col = {"bad": T['bad'], "warn": T['yel_fg'], "muted": T['ink']}[kind]
    bd = "border-bottom:1px solid %s;" % T['soft'] if i < len(todo) - 1 else ""
    todo_html.append('''        <div style="display:flex;flex-direction:column;gap:5px;padding:15px 16px;%s">
          <div style="display:flex;align-items:baseline;gap:8px"><span style="flex:1;font-size:13.5px;font-weight:600;color:%s">%s</span><span style="font-size:16px;font-weight:700;color:%s">%s</span></div>
          <p style="margin:0;font-size:12.5px;line-height:1.4;color:%s">%s</p>
        </div>''' % (bd, T['ink'], name, col, n, T['muted'], sub))

main_inner = rail(0) + '''

    <main style="display:flex;flex-direction:column;gap:18px;padding:26px 28px;min-width:0;overflow:hidden">
      <div style="display:flex;align-items:center;gap:14px;height:34px">
        <h1 style="margin:0;font-size:20px;font-weight:700;letter-spacing:-.01em;color:%(ink)s">闭环总览</h1>
        <span style="font-size:12.5px;color:%(muted)s">3 月 1 日 – 3 月 31 日</span>
        <div style="margin-left:auto;display:flex;align-items:center;gap:10px">
          <span style="display:flex;align-items:center;gap:7px;height:32px;padding:0 12px;border:1px solid %(line)s;border-radius:10px;font-size:12.5px;color:%(ink2)s">归因模型<span style="font-weight:600;color:%(ink)s">末次点击</span>%(chev)s</span>
          %(export)s
        </div>
      </div>

      <div style="display:grid;grid-template-columns:repeat(5, minmax(0, 1fr));gap:14px;height:100px">
%(kpis)s
      </div>

      <div style="height:346px;padding:18px 20px;border:1px solid %(line)s;border-radius:14px;display:flex;flex-direction:column;gap:12px">
        <div style="display:flex;align-items:center;gap:12px;height:30px">
          <span style="font-size:14px;font-weight:600;color:%(ink)s">全链路转化</span>
          <span style="font-size:12.5px;color:%(muted)s">每一步按联系人 ID 串联，可下钻到人 · 环比为该阶段人数变化</span>
          <span style="margin-left:auto;display:flex;align-items:center;gap:4px;font-size:12.5px;color:%(ink2)s">下钻%(chev)s</span>
        </div>
        <div style="display:flex;flex-direction:column">
%(frows)s
        </div>
      </div>

      <div style="height:266px;padding:18px 20px;border:1px solid %(line)s;border-radius:14px;display:flex;flex-direction:column;gap:12px">
        <div style="display:flex;align-items:center;gap:12px;height:30px">
          <span style="font-size:14px;font-weight:600;color:%(ink)s">渠道效果</span>
          <span style="font-size:12.5px;color:%(muted)s">收入按末次点击归因</span>
          <span style="margin-left:auto;font-size:12.5px;color:%(muted)s">合计 ROAS <span style="font-weight:700;color:%(ink)s">3.98</span></span>
        </div>
        <div style="display:flex;flex-direction:column">
          <div style="display:grid;grid-template-columns:%(cg)s;gap:14px;align-items:center;height:30px;border-bottom:1px solid %(line)s;font-size:11.5px;color:%(time)s">
            <span>渠道</span><span>花费</span><span>线索</span><span>成交</span><span>收入</span><span>线索成本</span><span style="justify-self:end">ROAS</span>
          </div>
%(crows)s
        </div>
      </div>
    </main>

    <aside style="border-left:1px solid %(line)s;display:flex;flex-direction:column;min-width:0">
      <div style="display:flex;align-items:center;gap:8px;padding:26px 16px 20px;border-bottom:1px solid %(line)s">
        <h2 style="margin:0;font-size:16px;font-weight:700;letter-spacing:-.01em;color:%(ink)s">今日待办</h2>
        <span style="min-width:20px;height:20px;padding:0 6px;display:flex;align-items:center;justify-content:center;border-radius:999px;background:%(brand)s;color:#ffffff;font-size:11.5px;font-weight:700">22</span>
      </div>
      <div style="display:flex;flex-direction:column">
%(todo)s
      </div>
      <div style="margin-top:auto;padding:18px 16px 22px;border-top:1px solid %(line)s;display:flex;flex-direction:column;gap:10px">
        <div style="display:flex;align-items:baseline"><span style="font-size:12.5px;color:%(muted)s">本月成交目标</span><span style="margin-left:auto;font-size:12.5px;font-weight:600;color:%(ink)s">74%%</span></div>
        <span style="position:relative;display:block;width:100%%;height:7px;border-radius:999px;background:%(gry_bg)s"><span style="position:absolute;left:0;top:0;width:74%%;height:7px;border-radius:999px;background:%(brand)s"></span></span>
        <span style="font-size:11.5px;color:%(time)s">HK$742,600 / HK$1,000,000</span>
      </div>
    </aside>
''' % dict(T, chev=ic("i-chevron", 14, "stroke-width:2;color:%s" % T['time']),
           export=btn_ghost("导出"),
           kpis="\n".join([
               kpi("广告花费", "HK$186,400", "较上月 +8.2%", "muted"),
               kpi("新增线索", "2,340", "较上月 +14.6%", "good"),
               kpi("线索→成交", "11.5%", "较上月 +1.8 个百分点", "good"),
               kpi("成交金额", "HK$742,600", "较上月 +21.4%", "good"),
               kpi("ROAS", "3.98", "较上月 +0.42", "good")]),
           frows="\n".join(frows), crows="\n".join(crows), cg=CG, todo="\n".join(todo_html))

write("Main", "72px minmax(0,1fr) 212px", main_inner)
print("Main.dc.html")


# ══ 2. 客服工作台 ════════════════════════════════════════
CONV = [
    ("陈晓琳", "14:04", "好，帮我下单", "付费搜索", "blue", True),
    ("黄志明", "14:01", "订单什么时候发货", "EDM 邮件", "gray", False),
    ("李佩珊", "13:58", "有没有优惠券可以用", "社媒广告", "blue", False),
    ("王家俊", "13:55", "买错了想退货", "自然搜索", "gray", False),
    ("张美玲", "13:51", "门店几点关门", "自然搜索", "gray", False),
    ("林卓豪", "13:47", "改一下收货地址", "付费搜索", "blue", False),
    ("何嘉怡", "13:42", "发票抬头写错了", "EDM 邮件", "gray", False),
    ("郑伟强", "13:38", "支持货到付款吗", "KOL 合作", "yellow", False),
]
crows = []
for i, (name, t, snip, src, kind, act) in enumerate(CONV):
    bg = "background:%s;" % T['brandsoft'] if act else ""
    bd = "" if i == len(CONV) - 1 else "border-bottom:1px solid %s;" % T['soft']
    crows.append('''        <div style="display:flex;gap:11px;padding:14px 16px;height:94px;%s%s">
          <span style="width:40px;height:40px;flex:none;border-radius:50%%;background:%s;color:%s;display:flex;align-items:center;justify-content:center;font-size:13.5px;font-weight:600">%s</span>
          <div style="flex:1;min-width:0;display:flex;flex-direction:column;gap:4px">
            <div style="display:flex;align-items:baseline;gap:8px"><span style="flex:1;min-width:0;font-size:14px;font-weight:600;color:%s;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">%s</span><span style="font-size:11.5px;color:%s">%s</span></div>
            <p style="margin:0;font-size:13.5px;line-height:1.36;color:%s;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">%s</p>
            <span style="align-self:flex-start">%s</span>
          </div>
        </div>''' % (bg, bd, T['gry_bg'], T['gry_fg'], name[0], T['ink'], name, T['time'], t,
                     T['muted'], snip, tag(src, kind)))

def bub_in(text, t, w=330):
    return '''        <div style="display:flex">
          <div style="position:relative;max-width:%dpx;padding:9px 11px 8px;border-radius:10px;border-top-left-radius:2px;background:%s;box-shadow:0 1px 1px rgba(16,24,40,.09);font-size:13.5px;line-height:1.45;color:%s">
            <p style="margin:0;padding-right:52px">%s</p>
            <span style="position:absolute;right:10px;bottom:6px;font-size:10.5px;color:%s">%s</span>
          </div>
        </div>''' % (w, T['surf'], T['ink'], text, T['time'], t)

def bub_out(text, t, w=350):
    return '''        <div style="display:flex;justify-content:flex-end">
          <div style="position:relative;max-width:%dpx;padding:9px 11px 8px;border-radius:10px;border-top-right-radius:2px;background:%s;box-shadow:0 1px 1px rgba(16,24,40,.09);font-size:13.5px;line-height:1.45;color:%s">
            <p style="margin:0;padding-right:60px">%s</p>
            <span style="position:absolute;right:10px;bottom:6px;display:flex;align-items:center;gap:3px;font-size:10.5px;color:%s">%s%s</span>
          </div>
        </div>''' % (w, T['accent'], T['ink'], text, T['time'], t,
                     ic("i-check2", 14, "stroke-width:2.2;color:%s" % T['tick']))

def chip(text):
    return ('<span style="align-self:center;padding:4px 12px;border-radius:999px;background:rgba(255,255,255,.75);'
            'font-size:11.5px;color:%s">%s</span>' % (T['muted'], text))

product_card = '''        <div style="display:flex;justify-content:flex-end">
          <div style="width:342px;padding:12px 14px;border-radius:10px;border-top-right-radius:2px;background:%s;box-shadow:0 1px 1px rgba(16,24,40,.09)">
            <div style="display:flex;align-items:baseline;gap:8px">
              <span style="font-size:14px;font-weight:600;color:%s">敏感肌修护套装 · 强化版</span>
            </div>
            <p style="margin:6px 0 0;font-size:13.5px;color:%s">精华 / 面霜 / 洁面 共 3 件 · 无酒精无香精</p>
            <div style="display:flex;align-items:baseline;gap:9px;margin-top:6px">
              <span style="font-size:14px;font-weight:700;color:%s">HK$1,280</span>
              <span style="font-size:12.5px;color:%s;text-decoration:line-through">HK$1,480</span>
              <span>%s</span>
            </div>
            <div style="height:1px;background:%s;margin:11px 0 9px"></div>
            <div style="display:flex;align-items:center;gap:7px">
              <span style="flex:1;font-size:12.5px;font-weight:600;color:%s">已按老客身份自动应用 9 折</span>
              <span style="font-size:10.5px;color:%s">14:03</span>
            </div>
          </div>
        </div>''' % (T['surf'], T['ink'], T['ink2'], T['ink'], T['time'], tag("老客价", "green"), T['line'], T['grn_fg'], T['time'])

stream = "\n".join([
    chip("今天 14:00"),
    bub_in("上次买的修护精华用完了，<br>想再入一套", "14:00"),
    bub_out("陈小姐你好！看到你 3 月买的是敏感肌<br>修护套装。这次要不要试试强化版？", "14:00"),
    bub_in("有什么不一样吗", "14:02"),
    product_card,
    bub_in("会员价是怎么算的", "14:04"),
    bub_out("你是第二次购买，自动 9 折；<br>另外还有一张 HK$100 老客券可叠加。", "14:04"),
    bub_in("好，帮我下单", "14:05"),
])

def kv(k, v, vcol=None):
    return ('<div style="display:flex;align-items:baseline;gap:10px"><span style="font-size:12.5px;color:%s">%s</span>'
            '<span style="margin-left:auto;font-size:13.5px;font-weight:500;color:%s;text-align:right">%s</span></div>'
            % (T['muted'], k, vcol or T['ink'], v))

inbox_inner = rail(1) + '''

    <section style="display:flex;flex-direction:column;border-right:1px solid %(line)s;min-width:0">
%(phead)s
      <div style="display:flex;gap:20px;padding:0 18px;border-bottom:1px solid %(line)s">
        <span style="padding:6px 0 8px;font-size:13.5px;font-weight:600;color:%(ink)s;box-shadow:inset 0 -2.5px 0 %(brand)s">全部 <span style="color:%(brand)s">34</span></span>
        <span style="padding:6px 0 8px;font-size:13.5px;font-weight:600;color:%(muted)s">我的 <span style="color:%(time)s">12</span></span>
        <span style="padding:6px 0 8px;font-size:13.5px;font-weight:600;color:%(muted)s">未分配 <span style="color:%(time)s">7</span></span>
      </div>
      <div style="display:flex;flex-direction:column">
%(crows)s
      </div>
    </section>

    <section style="display:flex;flex-direction:column;min-width:0">
      <div style="display:flex;align-items:center;gap:11px;padding:19px 18px;border-bottom:1px solid %(line)s">
        <span style="width:42px;height:42px;flex:none;border-radius:50%%;background:%(gry_bg)s;color:%(gry_fg)s;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:600">陈</span>
        <div style="min-width:0">
          <p style="margin:0;display:flex;align-items:center;gap:7px;font-size:16px;font-weight:700;letter-spacing:-.01em;color:%(ink)s">陈晓琳 %(oldtag)s</p>
          <p style="margin:1px 0 0;font-size:12.5px;color:%(muted)s">+852 9123 4567 · 网页组件 · 会话 c-31184</p>
        </div>
        <div style="margin-left:auto;display:flex;gap:2px;color:%(gry_fg)s">%(hicons)s</div>
      </div>

      <div style="flex:1;display:flex;flex-direction:column;gap:17px;padding:20px 26px 9px;background:%(warm)s;min-height:0;overflow:hidden">
%(stream)s
      </div>

      <div style="display:flex;align-items:center;gap:4px;padding:10px 16px;border-top:1px solid %(line)s;background:%(surf)s">
        <span style="width:34px;height:34px;display:flex;align-items:center;justify-content:center;border-radius:7px;color:%(gry_fg)s">%(emoji)s</span>
        <span style="width:34px;height:34px;display:flex;align-items:center;justify-content:center;border-radius:7px;color:%(gry_fg)s">%(clip)s</span>
        <span style="flex:1;min-width:0;height:40px;margin:0 6px;padding:0 16px;display:flex;align-items:center;border-radius:999px;background:#f4f5f6;font-size:13.5px;color:#a3aab3">回复 陈晓琳…</span>
        <span style="width:34px;height:34px;display:flex;align-items:center;justify-content:center;border-radius:7px;color:%(ink)s">%(mic)s</span>
      </div>
    </section>

    <aside style="border-left:1px solid %(line)s;display:flex;flex-direction:column;min-width:0;overflow:hidden">
      <div style="padding:22px 18px 18px;border-bottom:1px solid %(line)s;display:flex;flex-direction:column;gap:9px">
        <div style="display:flex;align-items:center;gap:8px">
          <h2 style="margin:0;font-size:16px;font-weight:700;letter-spacing:-.01em;color:%(ink)s">客户档案</h2>
          <span style="margin-left:auto">%(oldtag)s</span>
        </div>
        <span style="font-size:12.5px;color:%(muted)s">首次接触 3 月 14 日 · 第 25 天</span>
      </div>

      <div style="padding:16px 18px;border-bottom:1px solid %(line)s;display:flex;flex-direction:column;gap:10px">
        <span style="font-size:11.5px;font-weight:600;letter-spacing:.04em;color:%(time)s">来源归因</span>
        %(kv1)s
        %(kv2)s
      </div>

      <div style="padding:16px 18px;border-bottom:1px solid %(line)s;display:flex;flex-direction:column;gap:10px">
        <span style="font-size:11.5px;font-weight:600;letter-spacing:.04em;color:%(time)s">交易</span>
        %(kv3)s
        %(kv4)s
        %(kv5)s
      </div>

      <div style="padding:16px 18px;border-bottom:1px solid %(line)s;display:flex;flex-direction:column;gap:10px">
        <span style="font-size:11.5px;font-weight:600;letter-spacing:.04em;color:%(time)s">当前商机</span>
        <div style="padding:10px 12px;border-radius:10px;background:%(brandsoft)s;display:flex;flex-direction:column;gap:5px">
          <span style="font-size:13.5px;font-weight:600;color:%(ink)s">强化版套装 HK$1,280</span>
          <span style="font-size:11.5px;color:%(grn_fg)s">报价中 · 负责人 Kelvin</span>
        </div>
      </div>

      <div style="padding:16px 18px;border-bottom:1px solid %(line)s;display:flex;flex-direction:column;gap:10px">
        <span style="font-size:11.5px;font-weight:600;letter-spacing:.04em;color:%(time)s">行为足迹</span>
        %(kv6)s
        %(kv7)s
      </div>

      <div style="padding:16px 18px;display:flex;flex-direction:column;gap:9px">
        %(btn360)s
      </div>
    </aside>
''' % dict(T,
    phead=panel_head("会话", icon_btn("i-search") + icon_btn("i-filter")),
    crows="\n".join(crows), stream=stream,
    oldtag=tag("老客", "green"),
    hicons=icon_btn("i-search") + icon_btn("i-info") + icon_btn("i-more"),
    emoji=ic("i-emoji"), clip=ic("i-clip"), mic=ic("i-mic"),
    kv1=kv("首触", "付费搜索<br><span style='font-size:11.5px;color:%s'>春季护肤 · 3/14</span>" % T['muted']),
    kv2=kv("末触", "EDM 邮件<br><span style='font-size:11.5px;color:%s'>老客召回 · 4/2</span>" % T['muted']),
    kv3=kv("历史订单", "2 单"),
    kv4=kv("累计消费", "HK$1,860"),
    kv5=kv("客单价", "HK$930"),
    kv6=kv("进站", "9 次"),
    kv7=kv("点击", "24 次"),
    btn360='<span style="display:flex;align-items:center;justify-content:center;gap:7px;height:38px;border-radius:10px;background:%s;color:#ffffff;font-size:13.5px;font-weight:600">查看 360 全链路</span>' % T['brand'])

write("Inbox", "72px 292px minmax(0,1fr) 212px", inbox_inner)
print("Inbox.dc.html")


# ══ 3. 客户 360 全链路 ═══════════════════════════════════
# 类型色：营销蓝 / 客服灰 / 销售绿。全部事件都挂在同一个联系人 ID 上。
TL = [
    ("03-14", "09:12", "营销", "blue",  "广告曝光",     "Google Ads「春季护肤」· 关键词「敏感肌 洁面」· 搜索首位"),
    ("03-14", "09:12", "营销", "blue",  "点击广告",     "gclid=Cj0KCQjw…8f2 · iPhone 15 · 香港 · 单次点击 HK$4.20"),
    ("03-14", "09:13", "营销", "blue",  "进入落地页",   "/skincare-starter · 停留 1 分 42 秒 · 滚动 78%"),
    ("03-14", "09:15", "营销", "blue",  "点击「立即咨询」", "首屏 CTA · 表单未填，直接开会话"),
    ("03-14", "09:15", "客服", "gray",  "首次会话",     "网页组件 · 客服 Amy · 3 轮 · 时长 7 分"),
    ("03-14", "09:22", "销售", "green", "创建线索",     "评分 72 · 来源 付费搜索 / 春季护肤 · 分配给 Kelvin"),
    ("03-16", "14:03", "营销", "blue",  "打开邮件",     "「敏感肌护理指南」· 点击 1 次 · 活动 新客培育"),
    ("03-18", "11:20", "销售", "green", "创建商机",     "敏感肌修护套装 · HK$1,280 · 阶段 报价中"),
    ("03-19", "16:45", "销售", "green", "发送报价",     "报价单 Q-1042 · 有效期 7 天 · 已查看 2 次"),
    ("03-21", "10:08", "销售", "green", "成交",         "订单 SO-20481 · HK$1,180（新客券 −HK$100）"),
    ("03-24", "09:30", "客服", "gray",  "售后咨询",     "退货政策 · 已解决 · 满意度 5 / 5"),
    ("04-02", "20:11", "销售", "green", "复购",         "订单 SO-21107 · HK$680 · 末次触点 EDM / 老客召回"),
    ("04-08", "14:00", "客服", "gray",  "会话进行中",   "强化版套装咨询 · 已建商机 HK$1,280 · 客服 Amy"),
]
DOT = {"blue": T['blue_fg'], "gray": T['gry_fg'], "green": T['grn_fg']}
tl_rows = []
for i, (d, t, kind, ck, title, detail) in enumerate(TL):
    last = (i == len(TL) - 1)
    line = ("" if last else
            '<span style="position:absolute;left:11px;top:14px;bottom:-14px;width:1.5px;background:%s"></span>' % T['line'])
    cur = ('background:%s;border-radius:10px;' % T['brandsoft']) if last else ""
    tl_rows.append('''            <div style="display:grid;grid-template-columns:88px 24px minmax(0,1fr);gap:12px;min-height:54px;%s">
              <span style="padding-top:7px;font-size:11.5px;color:%s;text-align:right;white-space:nowrap">%s<br><span style="color:%s">%s</span></span>
              <span style="position:relative">%s<span style="position:absolute;left:7px;top:10px;width:9px;height:9px;border-radius:50%%;background:%s;box-shadow:0 0 0 3px #ffffff"></span></span>
              <div style="display:flex;flex-direction:column;gap:3px;padding:5px 12px 5px 0;min-width:0">
                <div style="display:flex;align-items:center;gap:9px">%s<span style="font-size:13.5px;font-weight:600;color:%s">%s</span></div>
                <span style="font-size:11.5px;line-height:1.45;color:%s;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">%s</span>
              </div>
            </div>''' % (cur, T['muted'], d, T['time'], t, line, DOT[ck],
                         tag(kind, ck), T['ink'], title, T['muted'], detail))

CUST = [
    ("陈晓琳", "老客",   "green",  "HK$1,860", "付费搜索", True),
    ("黄志明", "老客",   "green",  "HK$2,240", "EDM 邮件", False),
    ("李佩珊", "商机",   "yellow", "HK$0",     "社媒广告", False),
    ("王家俊", "老客",   "green",  "HK$680",   "自然搜索", False),
    ("张美玲", "线索",   "blue",   "HK$0",     "自然搜索", False),
    ("林卓豪", "商机",   "yellow", "HK$1,180", "付费搜索", False),
    ("何嘉怡", "老客",   "green",  "HK$3,420", "EDM 邮件", False),
]
cust_rows = []
for i, (name, stage, sk, ltv, src, act) in enumerate(CUST):
    bg = "background:%s;" % T['brandsoft'] if act else ""
    bd = "" if i == len(CUST) - 1 else "border-bottom:1px solid %s;" % T['soft']
    cust_rows.append('''        <div style="display:flex;gap:11px;padding:15px 16px;%s%s">
          <span style="width:40px;height:40px;flex:none;border-radius:50%%;background:%s;color:%s;display:flex;align-items:center;justify-content:center;font-size:13.5px;font-weight:600">%s</span>
          <div style="flex:1;min-width:0;display:flex;flex-direction:column;gap:4px">
            <div style="display:flex;align-items:center;gap:8px"><span style="flex:1;min-width:0;font-size:14px;font-weight:600;color:%s">%s</span>%s</div>
            <span style="font-size:11.5px;color:%s">%s · 累计 %s</span>
          </div>
        </div>''' % (bg, bd, T['gry_bg'], T['gry_fg'], name[0], T['ink'], name, tag(stage, sk), T['muted'], src, ltv))

def kv2(k, v, vcol=None):
    return ('<div style="display:flex;align-items:baseline;gap:10px"><span style="font-size:12.5px;color:%s">%s</span>'
            '<span style="margin-left:auto;font-size:13.5px;font-weight:500;color:%s;text-align:right">%s</span></div>'
            % (T['muted'], k, vcol or T['ink'], v))

c360_inner = rail(2) + '''

    <section style="display:flex;flex-direction:column;border-right:1px solid %(line)s;min-width:0">
%(phead)s
      <div style="padding:0 18px 14px">
        <span style="display:flex;align-items:center;gap:8px;height:36px;padding:0 12px;border-radius:999px;background:#f4f5f6;font-size:13.5px;color:#a3aab3">%(sicon)s搜索姓名、电话、订单号…</span>
      </div>
      <div style="display:flex;flex-direction:column;border-top:1px solid %(line)s">
%(cust)s
      </div>
    </section>

    <section style="display:flex;flex-direction:column;min-width:0">
      <div style="display:flex;align-items:center;gap:11px;padding:19px 20px;border-bottom:1px solid %(line)s">
        <span style="width:42px;height:42px;flex:none;border-radius:50%%;background:%(gry_bg)s;color:%(gry_fg)s;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:600">陈</span>
        <div style="min-width:0">
          <p style="margin:0;display:flex;align-items:center;gap:7px;font-size:20px;font-weight:700;letter-spacing:-.01em;color:%(ink)s">陈晓琳 %(oldtag)s</p>
          <p style="margin:2px 0 0;font-size:11.5px;color:%(muted)s">contact_id c-8821 · 全链路 13 个事件 · 首次接触至今 25 天</p>
        </div>
        <div style="margin-left:auto;display:flex;align-items:center;gap:8px">%(ghost)s%(prim)s</div>
      </div>

      <div style="flex:1;min-height:0;overflow:hidden;padding:10px 20px 0">
        <div style="display:flex;flex-direction:column">
%(tl)s
        </div>
      </div>
    </section>

    <aside style="border-left:1px solid %(line)s;display:flex;flex-direction:column;min-width:0;overflow:hidden">
%(ahead)s
      <div style="padding:16px 18px;border-bottom:1px solid %(line)s;display:flex;flex-direction:column;gap:10px">
        <span style="font-size:11.5px;font-weight:600;letter-spacing:.04em;color:%(time)s">归因</span>
        %(k1)s
        %(k2)s
        %(k3)s
      </div>
      <div style="padding:16px 18px;border-bottom:1px solid %(line)s;display:flex;flex-direction:column;gap:10px">
        <span style="font-size:11.5px;font-weight:600;letter-spacing:.04em;color:%(time)s">价值</span>
        %(k4)s
        %(k5)s
        %(k6)s
        %(k7)s
      </div>
      <div style="padding:16px 18px;border-bottom:1px solid %(line)s;display:flex;flex-direction:column;gap:10px">
        <span style="font-size:11.5px;font-weight:600;letter-spacing:.04em;color:%(time)s">行为足迹</span>
        %(k8)s
        %(k9)s
        %(k10)s
      </div>
      <div style="padding:16px 18px;display:flex;flex-direction:column;gap:10px">
        <span style="font-size:11.5px;font-weight:600;letter-spacing:.04em;color:%(time)s">标签</span>
        <div style="display:flex;flex-wrap:wrap;gap:8px">%(tags)s</div>
      </div>
    </aside>
''' % dict(T,
    phead=panel_head("客户", icon_btn("i-filter"), sub="2,340 位 · 本月新增 412"),
    sicon=ic("i-search", 16, "color:#a3aab3"), cust="\n".join(cust_rows), tl="\n".join(tl_rows),
    oldtag=tag("老客", "green"), ghost=btn_ghost("合并重复"), prim=btn_primary("新建商机", "i-plus"),
    ahead=aside_head("客户档案", "+852 9123 4567"),
    k1=kv2("首次触点", "付费搜索<br><span style='font-size:11.5px;color:%s'>春季护肤 · 3/14 09:12</span>" % T['muted']),
    k2=kv2("末次触点", "EDM 邮件<br><span style='font-size:11.5px;color:%s'>老客召回 · 4/2 20:11</span>" % T['muted']),
    k3=kv2("获客成本", "HK$90"),
    k4=kv2("订单", "2 单"),
    k5=kv2("累计消费", "HK$1,860"),
    k6=kv2("客单价", "HK$930"),
    k7=kv2("预估 LTV", "HK$3,100", T['grn_fg']),
    k8=kv2("进站", "9 次"),
    k9=kv2("点击", "24 次"),
    k10=kv2("会话", "3 次"),
    tags="".join([tag("敏感肌", "gray"), tag("高意向", "yellow"), tag("价格敏感", "gray"), tag("复购客", "green")]))

write("Contact360", "72px 292px minmax(0,1fr) 212px", c360_inner)
print("Contact360.dc.html")


# ══ 4. 线索池 ════════════════════════════════════════════
# 7 + 412 + 720 + 1,201 = 2,340，与总览一致；720 = 漏斗「商机」
LEAD_FILTERS = [("全部", "2,340", False), ("未分配", "7", False), ("跟进中", "412", True),
                ("已转商机", "720", False), ("已流失", "1,201", False)]
lf = []
for name, n, act in LEAD_FILTERS:
    st = "background:%s;font-weight:600;" % T['brandsoft'] if act else "font-weight:500;"
    lf.append('        <div style="display:flex;align-items:center;height:44px;padding:0 18px;%sfont-size:13.5px;color:%s"><span style="flex:1">%s</span><span style="font-size:12.5px;color:%s">%s</span></div>' % (st, T['ink'], name, T['time'], n))

LEADS = [
    ("陈晓琳", "付费搜索", "春季护肤",   92, "3/14 09:22", "已转商机", "green",  "Kelvin", True),
    ("李佩珊", "社媒广告", "短视频种草", 81, "4/07 21:40", "跟进中",   "blue",   "Kelvin", False),
    ("张美玲", "自然搜索", "—",          44, "4/08 13:51", "跟进中",   "blue",   "Sam",    False),
    ("林卓豪", "付费搜索", "敏感肌关键词", 77, "4/06 10:15", "已转商机", "green", "Kelvin", False),
    ("郑伟强", "KOL 合作", "美妆博主合作", 38, "4/08 13:38", "未分配",  "gray",   "—",      False),
    ("吴凯文", "EDM 邮件", "新客培育",   66, "4/05 18:02", "跟进中",   "blue",   "Sam",    False),
    ("周雅婷", "社媒广告", "图文轮播",   59, "4/07 15:26", "跟进中",   "blue",   "Ivy",    False),
    ("梁俊杰", "付费搜索", "品牌词",     71, "4/04 11:09", "跟进中",   "blue",   "Ivy",    False),
    ("徐婉婷", "自然搜索", "—",          29, "4/08 09:47", "未分配",   "gray",   "—",      False),
    ("罗志豪", "KOL 合作", "美妆博主合作", 24, "4/03 20:33", "已流失",  "yellow", "Sam",    False),
    ("许嘉敏", "EDM 邮件", "老客召回",   84, "4/02 20:11", "已转商机", "green",  "Kelvin", False),
]
LG = "minmax(0,1fr) 168px 96px 108px 96px 84px"
lrows = []
for i, (name, src, camp, score, first, status, sk, owner, act) in enumerate(LEADS):
    sel = "background:%s;" % T['brandsoft'] if act else ""
    bd = "" if i == len(LEADS) - 1 else "border-bottom:1px solid %s;" % T['soft']
    scol = T['ser1'] if score >= 70 else (T['warn'] if score >= 40 else T['bad'])
    lrows.append('''          <div style="display:grid;grid-template-columns:%s;gap:12px;align-items:center;height:56px;padding:0 14px;%s%s">
            <span style="display:flex;align-items:center;gap:10px;min-width:0"><span style="width:30px;height:30px;flex:none;border-radius:50%%;background:%s;color:%s;display:flex;align-items:center;justify-content:center;font-size:12.5px;font-weight:600">%s</span><span style="font-size:13.5px;font-weight:600;color:%s">%s</span></span>
            <span style="min-width:0"><span style="display:block;font-size:13.5px;color:%s">%s</span><span style="display:block;font-size:11.5px;color:%s;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">%s</span></span>
            <span style="display:flex;align-items:center;gap:8px"><span style="position:relative;width:44px;height:6px;border-radius:999px;background:%s"><span style="position:absolute;left:0;top:0;width:%d%%;height:6px;border-radius:999px;background:%s"></span></span><span style="font-size:12.5px;font-weight:600;color:%s">%d</span></span>
            <span style="font-size:12.5px;color:%s">%s</span>
            <span>%s</span>
            <span style="font-size:13.5px;color:%s">%s</span>
          </div>''' % (LG, sel, bd, T['gry_bg'], T['gry_fg'], name[0], T['ink'], name,
                       T['ink'], src, T['time'], camp,
                       T['gry_bg'], score, scol, T['ink2'], score,
                       T['muted'], first, tag(status, sk), T['ink2'], owner))

score_rows = [("表单填写", "+20"), ("多次进站 ≥ 3", "+15"), ("打开报价单", "+25"), ("落地页停留 > 1 分钟", "+12"), ("首触为付费渠道", "+20")]
sc_html = "\n".join('        <div style="display:flex;align-items:baseline;gap:8px"><span style="flex:1;font-size:12.5px;color:%s">%s</span><span style="font-size:12.5px;font-weight:600;color:%s">%s</span></div>' % (T['ink2'], k, T['grn_fg'], v) for k, v in score_rows)

leads_inner = rail(3) + '''

    <section style="display:flex;flex-direction:column;border-right:1px solid %(line)s;min-width:0">
%(phead)s
      <div style="display:flex;flex-direction:column;padding:4px 0 10px;border-bottom:1px solid %(line)s">
%(filters)s
      </div>
      <div style="padding:18px 18px 10px"><span style="font-size:11.5px;font-weight:600;letter-spacing:.04em;color:%(time)s">按来源</span></div>
      <div style="display:flex;flex-direction:column;gap:2px;padding:0 6px">
        <div style="display:flex;align-items:center;height:36px;padding:0 12px;font-size:13.5px;color:%(ink)s"><span style="flex:1">付费搜索</span><span style="font-size:12.5px;color:%(time)s">1,024</span></div>
        <div style="display:flex;align-items:center;height:36px;padding:0 12px;font-size:13.5px;color:%(ink)s"><span style="flex:1">社媒广告</span><span style="font-size:12.5px;color:%(time)s">712</span></div>
        <div style="display:flex;align-items:center;height:36px;padding:0 12px;font-size:13.5px;color:%(ink)s"><span style="flex:1">EDM 邮件</span><span style="font-size:12.5px;color:%(time)s">286</span></div>
        <div style="display:flex;align-items:center;height:36px;padding:0 12px;font-size:13.5px;color:%(ink)s"><span style="flex:1">自然搜索</span><span style="font-size:12.5px;color:%(time)s">241</span></div>
        <div style="display:flex;align-items:center;height:36px;padding:0 12px;font-size:13.5px;color:%(ink)s"><span style="flex:1">KOL 合作</span><span style="font-size:12.5px;color:%(time)s">77</span></div>
      </div>
    </section>

    <main style="display:flex;flex-direction:column;gap:18px;padding:26px 28px;min-width:0;overflow:hidden">
      <div style="display:flex;align-items:center;gap:12px;height:34px">
        <h2 style="margin:0;font-size:20px;font-weight:700;letter-spacing:-.01em;color:%(ink)s">跟进中</h2>
        <span style="font-size:12.5px;color:%(muted)s">412 条 · 按评分排序</span>
        <div style="margin-left:auto;display:flex;align-items:center;gap:8px">%(ghost)s%(prim)s</div>
      </div>
      <div style="flex:none;border:1px solid %(line)s;border-radius:14px;overflow:hidden">
        <div style="display:grid;grid-template-columns:%(lg)s;gap:12px;align-items:center;height:42px;padding:0 14px;background:%(surf2)s;border-bottom:1px solid %(line)s;font-size:11.5px;color:%(time)s">
          <span>线索</span><span>来源 / 活动</span><span>评分</span><span>首次接触</span><span>状态</span><span>负责人</span>
        </div>
%(rows)s
      </div>
    </main>

    <aside style="border-left:1px solid %(line)s;display:flex;flex-direction:column;min-width:0;overflow:hidden">
%(ahead)s
      <div style="padding:16px 18px;border-bottom:1px solid %(line)s;display:flex;flex-direction:column;gap:9px">
        <div style="display:flex;align-items:baseline"><span style="font-size:11.5px;font-weight:600;letter-spacing:.04em;color:%(time)s">评分构成</span><span style="margin-left:auto;font-size:16px;font-weight:700;color:%(ink)s">92</span></div>
%(score)s
      </div>
      <div style="padding:16px 18px;border-bottom:1px solid %(line)s;display:flex;flex-direction:column;gap:10px">
        <span style="font-size:11.5px;font-weight:600;letter-spacing:.04em;color:%(time)s">来源链路</span>
        <p style="margin:0;font-size:12.5px;line-height:1.6;color:%(ink2)s">Google Ads「春季护肤」<br>→ 落地页 /skincare-starter<br>→ 点击「立即咨询」<br>→ 客服 Amy 会话 3 轮<br>→ 线索创建（09:22）</p>
      </div>
      <div style="padding:16px 18px;display:flex;flex-direction:column;gap:9px">
        <span style="display:flex;align-items:center;justify-content:center;height:38px;border-radius:10px;background:%(brand)s;color:#ffffff;font-size:13.5px;font-weight:600">转为商机</span>
        <span style="display:flex;align-items:center;justify-content:center;height:38px;border-radius:10px;background:%(surf2)s;color:%(ink2)s;font-size:13.5px;font-weight:600">改派负责人</span>
      </div>
    </aside>
''' % dict(T, phead=panel_head("线索", icon_btn("i-search")), filters="\n".join(lf), lg=LG,
           ghost=btn_ghost("筛选", "i-filter"), prim=btn_primary("新建线索", "i-plus"), rows="\n".join(lrows),
           ahead=aside_head("陈晓琳", "线索 L-20481 · 已转商机"), score=sc_html)
write("Leads", "72px 292px minmax(0,1fr) 212px", leads_inner)
print("Leads.dc.html")


# ══ 5. 销售管线 ══════════════════════════════════════════
# 24+31+22+12 = 89 个进行中；本月成交 268 / HK$742,600 与总览一致
STAGES = [
    ("新建",   "24", "HK$186,000", [("郑伟强", "HK$1,280", "KOL 合作", "yellow", "今天", "Sam"),
                                   ("徐婉婷", "HK$680",   "自然搜索", "gray",   "今天", "—"),
                                   ("周雅婷", "HK$1,480", "社媒广告", "blue",   "1 天", "Ivy"),
                                   ("吴凯文", "HK$2,140", "EDM 邮件", "gray",   "2 天", "Sam")]),
    ("跟进中", "31", "HK$402,000", [("李佩珊", "HK$1,280", "社媒广告", "blue",   "1 天", "Kelvin"),
                                   ("张美玲", "HK$680",   "自然搜索", "gray",   "1 天", "Sam"),
                                   ("梁俊杰", "HK$3,420", "付费搜索", "blue",   "4 天", "Ivy"),
                                   ("黄志明", "HK$1,180", "EDM 邮件", "gray",   "6 天", "Kelvin")]),
    ("报价中", "22", "HK$358,000", [("陈晓琳", "HK$1,280", "付费搜索", "blue",   "今天", "Kelvin"),
                                   ("林卓豪", "HK$2,560", "付费搜索", "blue",   "2 天", "Kelvin"),
                                   ("何嘉怡", "HK$4,100", "EDM 邮件", "gray",   "9 天", "Ivy")]),
    ("谈判中", "12", "HK$264,000", [("许嘉敏", "HK$5,800", "EDM 邮件", "gray",   "3 天", "Kelvin"),
                                   ("王家俊", "HK$1,180", "自然搜索", "gray",   "5 天", "Sam"),
                                   ("苏泽民", "HK$12,400", "付费搜索", "blue",  "11 天", "Ivy")]),
    ("本月成交", "268", "HK$742,600", [("高晓峰", "HK$2,140", "社媒广告", "blue", "今天", "Ivy"),
                                    ("蔡欣怡", "HK$1,280", "付费搜索", "blue",  "今天", "Kelvin"),
                                    ("邱志远", "HK$680",   "EDM 邮件", "gray",  "昨天", "Sam")]),
]
cols = []
for si, (stage, n, amt, cards) in enumerate(STAGES):
    won = (si == len(STAGES) - 1)
    ch = []
    for name, val, src, sk, age, owner in cards:
        hot = (name == "陈晓琳")
        stale = age[0].isdigit() and int(age.split()[0]) >= 7
        border = ("border:2px solid %s;box-shadow:0 0 0 4px %s" % (T['brand'], T['brandsoft'])) if hot else ("border:1px solid %s;box-shadow:0 1px 2px rgba(16,24,40,.04)" % T['line'])
        agecol = T['bad'] if stale else T['time']
        ch.append('''          <div style="padding:12px 13px;background:#ffffff;border-radius:12px;%s;display:flex;flex-direction:column;gap:8px">
            <div style="display:flex;align-items:center;gap:8px"><span style="flex:1;min-width:0;font-size:13.5px;font-weight:600;color:%s;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">%s</span><span style="font-size:13.5px;font-weight:700;color:%s">%s</span></div>
            <div style="display:flex;align-items:center;gap:8px">%s<span style="margin-left:auto;font-size:11.5px;color:%s">停留 %s</span></div>
            <div style="display:flex;align-items:center;gap:6px"><span style="width:20px;height:20px;border-radius:50%%;background:%s;color:%s;display:flex;align-items:center;justify-content:center;font-size:10.5px;font-weight:700">%s</span><span style="font-size:11.5px;color:%s">%s</span></div>
          </div>''' % (border, T['ink'], name, T['ink'], val, tag(src, sk), agecol, age,
                       T['gry_bg'], T['gry_fg'], owner[0], T['muted'], owner))
    headcol = T['grn_fg'] if won else T['ink']
    cols.append('''        <div style="display:flex;flex-direction:column;gap:10px;min-width:0">
          <div style="display:flex;flex-direction:column;gap:3px;padding:12px 13px;border-radius:12px;background:%s">
            <div style="display:flex;align-items:center;gap:8px"><span style="font-size:13.5px;font-weight:700;color:%s">%s</span><span style="font-size:12.5px;color:%s">%s</span></div>
            <span style="font-size:12.5px;color:%s">%s</span>
          </div>
%s
        </div>''' % (T['brandsoft'] if won else T['surf2'], headcol, stage, T['time'], n, T['muted'], amt, "\n".join(ch)))

pipe_inner = rail(4) + '''

    <main style="display:flex;flex-direction:column;gap:18px;padding:26px 28px;min-width:0;overflow:hidden">
      <div style="display:flex;align-items:center;gap:12px;height:34px">
        <h1 style="margin:0;font-size:20px;font-weight:700;letter-spacing:-.01em;color:%(ink)s">销售管线</h1>
        <span style="font-size:12.5px;color:%(muted)s">进行中 89 个 · HK$1,210,000 · 停留超 7 天标红</span>
        <div style="margin-left:auto;display:flex;align-items:center;gap:8px">
          <div style="display:flex;gap:2px;padding:3px;border-radius:10px;background:%(surf2)s">
            <span style="padding:4px 12px;border-radius:7px;background:#ffffff;box-shadow:0 1px 2px rgba(16,24,40,.06);font-size:12.5px;font-weight:600;color:%(ink)s">看板</span>
            <span style="padding:4px 12px;border-radius:7px;font-size:12.5px;color:%(muted)s">列表</span>
          </div>
          %(ghost)s%(prim)s
        </div>
      </div>
      <div style="display:grid;grid-template-columns:repeat(5, minmax(0, 1fr));gap:14px;align-items:start">
%(cols)s
      </div>
    </main>

    <aside style="border-left:1px solid %(line)s;display:flex;flex-direction:column;min-width:0;overflow:hidden">
%(ahead)s
      <div style="padding:16px 18px;border-bottom:1px solid %(line)s;display:flex;flex-direction:column;gap:10px">
        <span style="font-size:11.5px;font-weight:600;letter-spacing:.04em;color:%(time)s">加权预测</span>
        <span style="font-size:24px;font-weight:700;letter-spacing:-.02em;color:%(ink)s;line-height:1.1">HK$486,000</span>
        <span style="font-size:11.5px;color:%(muted)s">按阶段成交概率 10 / 30 / 55 / 75%% 折算</span>
      </div>
      <div style="padding:16px 18px;border-bottom:1px solid %(line)s;display:flex;flex-direction:column;gap:10px">
        <span style="font-size:11.5px;font-weight:600;letter-spacing:.04em;color:%(time)s">按来源的成交率</span>
%(srcrate)s
      </div>
      <div style="padding:16px 18px;border-bottom:1px solid %(line)s;display:flex;flex-direction:column;gap:10px">
        <span style="font-size:11.5px;font-weight:600;letter-spacing:.04em;color:%(time)s">平均周期</span>
        %(cyc1)s
        %(cyc2)s
      </div>
      <div style="padding:16px 18px;display:flex;flex-direction:column;gap:10px">
        <div style="display:flex;align-items:baseline"><span style="font-size:12.5px;color:%(muted)s">本月目标</span><span style="margin-left:auto;font-size:12.5px;font-weight:600;color:%(ink)s">74%%</span></div>
        <span style="position:relative;display:block;width:100%%;height:7px;border-radius:999px;background:%(gry_bg)s"><span style="position:absolute;left:0;top:0;width:74%%;height:7px;border-radius:999px;background:%(brand)s"></span></span>
      </div>
    </aside>
''' % dict(T, ghost=btn_ghost("筛选", "i-filter"), prim=btn_primary("新建商机", "i-plus"), cols="\n".join(cols),
           ahead=aside_head("管线汇总", "3 月 · 5 个阶段"),
           srcrate="\n".join('        <div style="display:flex;align-items:center;gap:8px"><span style="flex:1;font-size:12.5px;color:%s">%s</span><span style="position:relative;width:56px;height:6px;border-radius:999px;background:%s"><span style="position:absolute;left:0;top:0;width:%d%%;height:6px;border-radius:999px;background:%s"></span></span><span style="width:34px;text-align:right;font-size:12.5px;font-weight:600;color:%s">%d%%</span></div>'
                             % (T['ink2'], s, T['gry_bg'], r, T['ser1'], T['ink2'], r)
                             for s, r in [("EDM 邮件", 58), ("付费搜索", 39), ("自然搜索", 35), ("社媒广告", 33), ("KOL 合作", 22)]),
           cyc1=kv2("线索 → 商机", "4.2 天"), cyc2=kv2("商机 → 成交", "6.8 天"))
write("Pipeline", "72px minmax(0,1fr) 212px", pipe_inner)
print("Pipeline.dc.html")


# ══ 6. 营销归因 ══════════════════════════════════════════
# 每个渠道下的活动加总 = 总览「渠道效果」那一行；ROAS = 收入 / 花费
CAMP = [
    ("付费搜索", "HK$92,400", "1,024", "118", "HK$341,200", "3.69", [
        ("春季护肤",     "HK$52,400", "21,300", "612", "184", "71", "HK$208,400", "3.98"),
        ("敏感肌关键词", "HK$28,000", "11,400", "298",  "92", "33", "HK$92,800",  "3.31"),
        ("品牌词",       "HK$12,000",  "4,100", "114",  "38", "14", "HK$40,000",  "3.33")]),
    ("社媒广告", "HK$61,800", "712", "79", "HK$219,400", "3.55", [
        ("短视频种草",   "HK$38,800", "9,800",  "449", "131", "51", "HK$141,600", "3.65"),
        ("图文轮播",     "HK$23,000", "5,600",  "263",  "78", "28", "HK$77,800",  "3.38")]),
    ("EDM 邮件", "HK$8,200", "286", "41", "HK$118,600", "14.46", [
        ("老客召回",     "HK$4,200",  "2,900",  "158",  "64", "26", "HK$78,200",  "18.62"),
        ("新客培育",     "HK$4,000",  "2,400",  "128",  "41", "15", "HK$40,400",  "10.10")]),
    ("自然搜索", "—", "241", "22", "HK$48,900", "—", [
        ("自然流量",     "—",         "3,100",  "241",  "68", "22", "HK$48,900",  "—")]),
    ("KOL 合作", "HK$24,000", "77", "8", "HK$14,500", "0.60", [
        ("美妆博主合作", "HK$24,000", "2,700",   "77",  "24",  "8", "HK$14,500",  "0.60")]),
]
AG = "minmax(0,1fr) 100px 84px 84px 84px 84px 116px 76px"
arows = []
for ch, spend, leads, deals, rev, roas, camps in CAMP:
    loss = (roas not in ("—",) and float(roas) < 1)
    arows.append('''          <div style="display:grid;grid-template-columns:%s;gap:14px;align-items:center;height:30px;padding:0 14px;background:%s;border-bottom:1px solid %s">
            <span style="font-size:12.5px;font-weight:700;color:%s">%s</span>
            <span style="font-size:12.5px;font-weight:600;color:%s">%s</span><span></span>
            <span style="font-size:12.5px;font-weight:600;color:%s">%s</span><span></span>
            <span style="font-size:12.5px;font-weight:600;color:%s">%s</span>
            <span style="font-size:12.5px;font-weight:600;color:%s">%s</span>
            <span style="justify-self:end;font-size:12.5px;font-weight:700;color:%s">%s</span>
          </div>''' % (AG, T['surf2'], T['line'], T['ink'], ch, T['ink2'], spend, T['ink2'], leads,
                       T['ink2'], deals, T['ink2'], rev, T['bad'] if loss else T['ink'], roas))
    for cname, cs, clicks, cl, opp, cd, crev, cr in camps:
        closs = (cr != "—" and float(cr) < 1)
        arows.append('''          <div style="display:grid;grid-template-columns:%s;gap:14px;align-items:center;height:37px;padding:0 14px 0 28px;border-bottom:1px solid %s">
            <span style="font-size:13.5px;color:%s">%s</span>
            <span style="font-size:13.5px;color:%s">%s</span>
            <span style="font-size:13.5px;color:%s">%s</span>
            <span style="font-size:13.5px;color:%s">%s</span>
            <span style="font-size:13.5px;color:%s">%s</span>
            <span style="font-size:13.5px;font-weight:600;color:%s">%s</span>
            <span style="font-size:13.5px;color:%s">%s</span>
            <span style="justify-self:end;font-size:13.5px;font-weight:700;color:%s">%s</span>
          </div>''' % (AG, T['soft'], T['ink'], cname, T['ink2'], cs, T['ink2'], clicks, T['ink2'], cl,
                       T['ink2'], opp, T['ink'], cd, T['ink2'], crev, T['bad'] if closs else T['ink'], cr))

models = [("首次点击", "谁把人带进来", False), ("末次点击", "谁促成了成交", True),
          ("线性", "每个触点平分", False), ("时间衰减", "越靠近成交权重越高", False)]
mh = []
for name, desc, act in models:
    st = ("background:%s;border:1px solid %s;" % (T['brandsoft'], T['brand'])) if act else ("border:1px solid %s;" % T['line'])
    mh.append('''        <div style="display:flex;flex-direction:column;gap:2px;padding:11px 14px;border-radius:10px;%s">
          <span style="font-size:13.5px;font-weight:600;color:%s">%s</span>
          <span style="font-size:11.5px;color:%s">%s</span>
        </div>''' % (st, T['ink'], name, T['muted'], desc))

# 同一笔收入在不同模型下的归属差异 —— 这就是为什么要选模型
CMP = [("付费搜索", "HK$412,300", "HK$341,200", "HK$368,900"),
       ("EDM 邮件", "HK$61,800",  "HK$118,600", "HK$92,400"),
       ("社媒广告", "HK$188,700", "HK$219,400", "HK$201,600")]
cmp_rows = "\n".join('''          <div style="display:grid;grid-template-columns:minmax(0,1fr) 128px 128px 128px;gap:14px;align-items:center;height:30px;border-bottom:1px solid %s">
            <span style="font-size:13.5px;font-weight:600;color:%s">%s</span>
            <span style="font-size:13.5px;color:%s">%s</span>
            <span style="font-size:13.5px;font-weight:700;color:%s">%s</span>
            <span style="font-size:13.5px;color:%s">%s</span>
          </div>''' % (T['soft'], T['ink'], c, T['ink2'], a, T['ink'], b, T['ink2'], d) for c, a, b, d in CMP)

attr_inner = rail(5) + '''

    <section style="display:flex;flex-direction:column;border-right:1px solid %(line)s;min-width:0">
%(phead)s
      <div style="padding:6px 18px 12px"><span style="font-size:11.5px;font-weight:600;letter-spacing:.04em;color:%(time)s">归因模型</span></div>
      <div style="display:flex;flex-direction:column;gap:8px;padding:0 18px 18px;border-bottom:1px solid %(line)s">
%(models)s
      </div>
      <div style="padding:18px 18px 10px"><span style="font-size:11.5px;font-weight:600;letter-spacing:.04em;color:%(time)s">回看窗口</span></div>
      <div style="display:flex;gap:2px;margin:0 18px;padding:3px;border-radius:10px;background:%(surf2)s">
        <span style="flex:1;text-align:center;padding:5px 0;border-radius:7px;font-size:12.5px;color:%(muted)s">7 天</span>
        <span style="flex:1;text-align:center;padding:5px 0;border-radius:7px;background:#ffffff;box-shadow:0 1px 2px rgba(16,24,40,.06);font-size:12.5px;font-weight:600;color:%(ink)s">30 天</span>
        <span style="flex:1;text-align:center;padding:5px 0;border-radius:7px;font-size:12.5px;color:%(muted)s">90 天</span>
      </div>
    </section>

    <main style="display:flex;flex-direction:column;gap:18px;padding:26px 28px;min-width:0;overflow:hidden">
      <div style="display:flex;align-items:center;gap:12px;height:34px">
        <h2 style="margin:0;font-size:20px;font-weight:700;letter-spacing:-.01em;color:%(ink)s">活动效果</h2>
        <span style="font-size:12.5px;color:%(muted)s">末次点击 · 30 天 · 3 月</span>
        <div style="margin-left:auto;display:flex;align-items:center;gap:8px">%(ghost)s%(prim)s</div>
      </div>

      <div style="flex:none;border:1px solid %(line)s;border-radius:14px;overflow:hidden">
        <div style="display:grid;grid-template-columns:%(ag)s;gap:14px;align-items:center;height:42px;padding:0 14px;border-bottom:1px solid %(line)s;font-size:11.5px;color:%(time)s">
          <span>渠道 / 活动</span><span>花费</span><span>点击</span><span>线索</span><span>商机</span><span>成交</span><span>收入</span><span style="justify-self:end">ROAS</span>
        </div>
%(rows)s
      </div>

      <div style="flex:none;padding:14px 20px 10px;border:1px solid %(line)s;border-radius:14px;display:flex;flex-direction:column;gap:8px">
        <div style="display:flex;align-items:center;gap:12px;height:26px">
          <span style="font-size:14px;font-weight:600;color:%(ink)s">同一笔收入，不同模型怎么分</span>
          <span style="font-size:12.5px;color:%(muted)s">EDM 在末次点击下被高估，付费搜索在首次点击下被高估 —— 决策前先定模型</span>
        </div>
        <div style="display:grid;grid-template-columns:minmax(0,1fr) 128px 128px 128px;gap:14px;align-items:center;height:26px;border-bottom:1px solid %(line)s;font-size:11.5px;color:%(time)s">
          <span>渠道</span><span>首次点击</span><span>末次点击 · 当前</span><span>线性</span>
        </div>
%(cmp)s
      </div>
    </main>
''' % dict(T, phead=panel_head("营销"), models="\n".join(mh), ag=AG, rows="\n".join(arows), cmp=cmp_rows,
           ghost=btn_ghost("导出"), prim=btn_primary("新建活动", "i-plus"))
write("Attribution", "72px 292px minmax(0,1fr)", attr_inner)
print("Attribution.dc.html")
