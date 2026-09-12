# 秒回 · 手机回复台 —— 设计稿（未确认，未搬）

v3（当前页，十四块画板）在 v2 之上并入第二轮九条盲点，含 Lucas 定的规则「SOS 任何值班的人都能接」；v2、v1 存档在画布第二、三页。内容与流程全部按 `lucaseng-star/jwc-bot` 的真实模式画：
SOS「等真人」队列（/api/escalations/active）、认领、🔴 我接管 / 停 bot、12 小时自动放回、
ChatDaddy 导入的话术库（/api/quick-replies）、IG/FB 号码交接（/api/igfb-handoffs）。
视觉沿用 `assets/ui-kit.css` 那套 token。

规则（Lucas，2026-09-12）：**设计确认之前，不往 jwc-bot 搬任何东西。**

- `*.dc.html` + `canvas.json`：画板源文件（可直接在设计画布里改）；`V1*.dc.html` 是存档
- `build_v3.py`：重新生成全部（v3 十四块 + 存档 v2 八块 + 存档 v1 六块 + 三页 canvas.json），`python3 build_v3.py`；`build_v2.py`、`build.py` 是它依赖的下层
- 人名、消息、价格皆为示例；价格真值只来自 Google Sheet 目录
