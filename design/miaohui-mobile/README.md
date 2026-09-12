# 秒回 · 手机回复台 —— 设计稿（未确认，未搬）

画布两页：**给员工看的**（11 屏，只放回复时用得上的东西）和 **参考 · 不进界面**（Telegram 零安装备选、英文界面、按渠道提示、规则与后端清单）。

内容与流程按 `lucaseng-star/jwc-bot` 的真实模式画：SOS 等真人队列、认领、停 bot、话术库（ChatDaddy 导入）、
IG/FB 号码交接、付款截图确认、24 小时窗口。视觉沿用 `assets/ui-kit.css` 那套 token。

规则（Lucas）：
- 设计确认之前，不往 jwc-bot 搬任何东西。
- SOS 任何值班的人都能接，先点先得。
- 界面上不出现接口名、规则、开关；那些只在参考页。

文件：
- `Notify / Main / Reply / Gate / Sent / Queue / Quick / Receipt / Failed / FailedWa / Login .dc.html`：员工看的 11 屏
- `TelegramReply / MainEn / SentMeta .dc.html`：参考页
- `V1* / V2*`：旧版存档，不在画布里（画布历史版本也留着）
- `build_v4.py`：重新生成当前画布（`python3 build_v4.py`，依赖 `build.py`、`build_v2.py` 里的小组件）
- 人名、消息、价格皆为示例；价格真值只来自 Google Sheet 目录
