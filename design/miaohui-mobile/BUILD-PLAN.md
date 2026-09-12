# 秒回 · 搬进 jwc-bot 的执行计划（待 Lucas 点头，点头前不动代码）

范围：只做画布 v4 的 11 屏。不碰 bot 的回复逻辑，不改 dashboard 现有功能（只加一处「X 在回」标签）。
以下每一条都对着 jwc-bot 现有代码写，没有猜的。

## 0 · 先量基线（1 天，可和开发并行）
- 只读脚本跑一遍 `leads.json`：每条 `escalation.history` 的 `askedAt` → `claimedAt` / `resolvedBy: manual_reply` 的时间差。
- 产出一个数字：过去 30 天 SOS → 首条人工回复的中位数。这是验收的对照基线。

## 1 · 后端（server.js + lib/，按这个顺序）
| # | 做什么 | 落在哪 | 备注 |
| --- | --- | --- | --- |
| 1.1 | 值班状态 | `lib/on-duty.js` + `GET/POST /api/duty`（adminAuth · sales） | 落盘 `DATA_DIR/on-duty.json`。SOS 收件人 = 值班名单；名单为空退回现状（现有 `getEscalationEmails/WANumbers`），否则 SOS 会没人收 |
| 1.2 | 认领不清 open | `POST /api/escalation/claim {chatId}` | 语义同现有 `GET /escalation/claim`，但只写 `open.claimedBy/claimedAt`，不移入 history；第二人 409 带 claimedBy。`/api/escalations/active` 的 `open[]` 带 claimedBy/claimedAt。手动回复收尾已存在（open → history, `resolvedBy: manual_reply`），不用改 |
| 1.3 | 跨线放行 | `guardChatBotScope` 加一条 | `lead.escalation.open.claimedBy === 我` 或 history 最近一条是我 → 放行 `/conversation/:chatId`、`/api/reply*`、`/api/takeover`。其它客人照旧挡。「我」= role 去掉 `sales_` 前缀 |
| 1.4 | 设备令牌 | `lib/device-token.js` + `/api/login` 加 `remember` + `resolveRole` 识别 + `GET /api/devices`、`POST /api/devices/:id/revoke`（owner） | **必须是新类型**，不是 staff-link：`/api/reply*` 挂着 `noLinkAuth`，签名链接刻意不能发消息，这条安全线不动。30 天，落盘 `devices.json`，可单独作废 |
| 1.5 | AI 草稿 | `POST /api/draft {chatId, lang}` → 3 条 `{answer, text}` | 复用现有 Claude 调用（`ANTHROPIC_MODEL`，默认 haiku 4.5）；输入 = 最近 6 条对话 + 目录事实（现有 catalog 缓存）+ 线的人设 + 语言；只出 JSON，不发送。约 US$0.004/次，日 100 次 ≈ US$12/月 |
| 1.6 | 翻译 | 复用 `/api/translate`（Google gtx，免费） | 现在只 zh/en，`target` 加 `ms`，一行改动 |
| 1.7 | Telegram | SOS 消息加 URL 按钮「打开回复」 | `sendTelegram` 已支持 ≤3 个 URL 按钮。深链 `/reply/?cid=…&t=…`，靠设备令牌登录，没登录落登录页。「在 Telegram 里直接回」第二阶段：记 SOS 的 message_id，收到 `reply_to_message` → 以线的人设 sendReply（现 webhook 只认「修 N」，要加分支） |
| 1.8 | dashboard | 客户行显示 `open.claimedBy` 「X 在回」 | 一处渲染，不改别的 |

## 2 · 前端（新页，同域）
- `reply.html` + `reply.js` + `reply.css`，`app.get('/reply', sendFile)` 加进现有静态白名单（仓库根目录不再整包静态服务，这是有意的）。加 manifest 供加到主屏幕。
- 调用方式沿用 dashboard：`x-admin-key` 头。用到的接口：`/api/escalations/active`、`/api/leads/:chatId`、`/api/reply`、`/api/reply-voice`、`/api/reply-media`、`/api/quick-replies`（+`/use/:id`）、`/api/takeover`、`/api/escalation/claim`、`/api/draft`、`/api/translate`、`/api/igfb-handoffs`（+`/contacted`）、`/verify`、`/reject`、`/api/duty`、`/api/whoami`。
- 11 屏照画布 v4；先中文，英文沿用 dashboard 的 i18n 字典做法；深色不做。
- 主号和桥接线（chatId 以 `wa:` 开头、或 botScope 是 main/jiajia/boon/lisa/saturnbird/amie）不进 app，前端按前缀隐藏。

## 3 · 测试与验收
- 每个新接口一支静态锁测试，照 `tests/` 的惯例（`node tests/x.test.js`，CI 跑 `npm test`）：认领不清 open；跨线只放行我认领的；设备令牌能回、link 令牌仍不能；值班名单为空退回现状。
- 手工：Boon 拿手机回 5 条 SOS，计时。目标：通知响 → 首句发出 < 60 秒。
- 上线前必验：暂停 bot 之后，排好的唤醒模板停不停（线上一条测试 lead）。代码里没找到明确答案。
- `PAUSE_AUTO_RESUME` 二选一：开，或把「12 小时后 Bot 接回」改成「Bot 不会自动回来」。

## 4 · 时间与熔断
- 物理极限：后端 1.1–1.4 + 前端 11 屏，3 天。现实：1–2 周，差额全是等验收、等部署、等同事试用。
- 熔断：上线两周，SOS → 首回中位数没降到基线的一半，停止投入。

## 5 · 风险
- `server.js` 4.5 万行单文件：改动小而集中，每处配测试，不顺手重构。
- `noLinkAuth` 是刻意的安全线：设备令牌是新类型，不放宽签名链接。
- 值班为空必须退回现状。
- 同一时间那边分支天天在提交：从 main 开新分支，小步合并，不长期分叉。
