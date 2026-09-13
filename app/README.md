# 秒回 v4 —— 手机回复台（可点原型）

一个只做一件事的手机页面：**客户在等真人，值班的人 60 秒内回掉。**

- 在线试用：<https://claude.ai/code/artifact/1d0b8666-ff40-4b49-9ab9-50972a5e99de>（手机打开即可）
- 本地：打开 `app/index.html`；iPhone Safari「添加到主屏幕」可当 app 用（有 manifest，全屏）。

## 它是什么、不是什么

- **是**：v4 设计稿的完整可点版本。登录 → 待回 → SOS 通知 → 会话 → 草稿/话术 → 发送 → 清队列 → 收款确认 → IG/FB 号码交接 → 发送失败处理，状态流转都是真的。
- **不是**：没接任何真实渠道。客户、消息、草稿、话术都是**示例数据**（`app.js` 顶部 `CONVS` / `HANDOFFS` / `TEMPLATES`）。
  接真数据 = 按 `design/miaohui-mobile/BUILD-PLAN.md` 搬进 jwc-bot，等设计确认后才动。

## 界面对应 bot 的哪些东西

| 界面 | bot 里的事实 |
| --- | --- |
| 🆘 等真人 列表，按等了多久排 | `/api/escalations/active`，最老的在最上 |
| 通知 → 点开就是那个客户，Bot 已停 | `/escalation/claim` 先点先得；接手即停 bot |
| 从列表点进去先看到「Bot 还在回，先停它」 | 只看不接手时 bot 仍在回；`🔴 停 bot 并回复` = takeover |
| 以 Emily / Cindy / Coco 的身份回复 | 客户只认识这个人设；员工名字只在后台 |
| 草稿 2 条 + 换一批 | Claude 按客户最后一句起草，只填输入框，发送必须你点 |
| BM 客户：中文写，发出时翻成 BM | `/api/translate`（示例先按草稿自带的 BM 发） |
| 已发 ✓✓ · 12 小时后 Bot 接回 · 交还 | 人工回复后 pause 12h，IG/FB 则永久转人手 |
| ✱ 话术：置顶 / 搜 / 文件夹 / 预览再发；输入框打 `/fcc` 直接弹 | `/api/quick-replies`（ChatDaddy 1,001 个 flow 原名原文）；搜索规则照 dashboard 的 `qrNormalizeQuery` / `qrMatches`：开头的 `/` 不算，名字、资料夹、每一步内文都搜 |
| 话术多步、带图、带 PDF、`{{name}}` | 发送顺序照 bot：每步先图（第一张带文字）→ 文件 → 剩下文字；`{{name}}` 填客户名 |
| 💳 客户付了？ 确认收款 / 不是付款 | `/verify` `/reject`，确认后 bot 自动发报名表 |
| IG/FB 给了号码 → 打开 WhatsApp / 已联系 | `/api/igfb-handoffs` |
| ❌ IG 窗口已关 / WhatsApp 窗口已关 | 24h 窗口；IG 改走 WhatsApp，WA 发唤醒模板 |
| 值班中 / 下班 | 下班不收通知；SOS 任何值班的人都能接 |

## 结构

```
app/
├── index.html            外壳：登录 / 待回 / 会话 / 号码交接 + 话术抽屉、预览、操作单、通知、toast
├── app.css               样式（--uk-* token → 组件；含深色）
├── app.js                示例数据、状态、渲染、交互
├── quick-reply-search.test.js  话术搜索守卫，用例跟 jwc-bot tests/quick-reply-search.test.js 一样（node app/quick-reply-search.test.js）
├── manifest.webmanifest  加到主屏幕
└── README.md
```

## 设计语言

沿用 `claude/ui-design-replication` 分支从收件箱 UI 复刻出来的 `assets/ui-kit.css`（`--uk-*` 变量）。
`app.css` 顶部 `[SYNC]` 段是那些 token 的副本，两条分支都进 main 后删掉、改 `@import` 即可。

等待时长颜色跟 bot 对客户的承诺走（"5-10 分钟真人回你"）：< 5 分绿，5–10 分黄，> 10 分红。

## 设计稿

`design/miaohui-mobile/`（Claude Design 画布），在线：<https://claude.ai/code/artifact/859aa1f3-ab17-47a3-aeed-45604a222923>
