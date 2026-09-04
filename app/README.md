# 秒回 —— 客户消息回复台（手机端）

一个只做一件事的手机 app：**把待回复的客户消息清零。**

打开 `app/index.html`（GitHub Pages 合并到 main 后是 `/app/`），
iPhone Safari「添加到主屏幕」即可当 app 用（有 manifest，standalone 全屏）。

## 它是什么、不是什么

- **是**：可点的完整原型。队列 → 会话 → 回复台 → 自动下一条，状态流转全是真的。
- **不是**：还没接任何真实渠道。消息、客户、草稿都是**示例数据**（`app.js` 顶部 `SAMPLE`）。

## 设计语言

沿用 `claude/ui-design-replication` 分支从收件箱 UI 复刻出来的 `assets/ui-kit.css`（`--uk-*` 变量）。
`app.css` 顶部 `[SYNC]` 段是那些 token 的副本，两条分支都进 main 后删掉、改 `@import` 即可。

手机端在此之上只加三样：触屏尺寸、等待时长语义色（红 ≥60 分 / 黄 ≥15 分 / 绿）、深色主题。

## 结构

```
app/
├── index.html            外壳：两屏（待回队列 / 会话）+ 回复台抽屉 + 两个操作单
├── app.css               样式（token → 组件，无写死数值）
├── app.js                状态、渲染、交互、示例数据、ChannelAdapter 契约
├── manifest.webmanifest  加到主屏幕
└── README.md
```

## 核心流程

1. **待回队列**：按「等了多久」排序，不是按「谁最新」。顶部三个数字：待回 / 今日已回 / 最久等待。
2. **⚡ 快速回**：列表里直接点，跳进会话并展开回复台，少一步。
3. **回复台**：AI 草稿（3 条，各带策略标签）/ 快捷话术（带 `{name}` `{course}` `{price}` 变量）/ 素材。
   语言 中 / EN / BM 跟客户走。**草稿只填进输入框，发送必须你点。**
4. **发送后**：会话自动移到「跟进中」；清队列模式下 0.9 秒后自动跳下一条。
5. **稍后跟进 / 标记完成 / 加标签**：一排三键，都会把会话带出待回队列。

## 接真实渠道

实现 `ChannelAdapter` 四个方法（见 `app.js` 顶部注释），替换 `const adapter = MockAdapter`：

| 渠道 | 方式 | 备注 |
| --- | --- | --- |
| WhatsApp | WhatsApp Business Cloud API | 官方，能收能发，模板消息需审核 |
| Instagram / Facebook | Meta Messenger Platform | 官方，客户发消息后 24 小时内可自由回复 |
| 小红书 | 无私信 API | 只能人工看；app 里已把「导到 WhatsApp」做成一条草稿 |

AI 草稿：`drafts` 字段现在是写死的。接入时由后端按「客户最后一句 + 课程资料 + 语言」生成，前端结构不变。
